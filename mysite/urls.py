"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from opentelemetry import trace, metrics
import logging

logger = logging.getLogger(__name__)
tracer = trace.get_tracer(__name__)
meter = metrics.get_meter(__name__)
hit_counter = meter.create_counter(
    "debug.hit_counter",
    unit="1",
    description="Number of times /debug/counter/ was hit",
)


def trigger_error(request):
    raise Exception("Test error for OneUptime monitoring")


def trigger_log(request):
    logger.info("test_log_event", extra={"event": "test_log_event", "user": "anonymous"})
    return HttpResponse("Log emitted")


def trigger_span(request):
    with tracer.start_as_current_span("test.span") as span:
        span.add_event("test_span_event", attributes={"event": "test_span_event", "user": "anonymous"})
    return HttpResponse("Span event emitted")


def trigger_counter(request):
    hit_counter.add(1, {"endpoint": "debug.counter", "env": "production"})
    return HttpResponse("Counter incremented")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('debug/error/', trigger_error),
    path('debug/log/', trigger_log),
    path('debug/span/', trigger_span),
    path('debug/counter/', trigger_counter),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

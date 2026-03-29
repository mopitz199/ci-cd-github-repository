from django.contrib import admin
from django.utils.html import format_html

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ("name", "age", "profile_image_preview")
	readonly_fields = ("profile_image_preview",)
	fields = ("name", "age", "profile_image")

	@admin.display(description="Image")
	def profile_image_preview(self, obj):
		if obj.profile_image:
			return format_html('<img src="{}" style="height: 60px; width: 60px; object-fit: cover; border-radius: 6px;" />', obj.profile_image.url)
		return "No image"

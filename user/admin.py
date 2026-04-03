from django.contrib import admin
from django.utils.html import format_html

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ("name", "age", "profile_image_preview", "identity_document_preview")
	readonly_fields = ("profile_image_preview", "identity_document_preview")
	fields = ("name", "age", "profile_image", "identity_document", "profile_image_preview", "identity_document_preview")

	@admin.display(description="Image")
	def profile_image_preview(self, obj):
		print("print image url", obj.profile_image.url)
		if obj.profile_image:
			return format_html('<img src="{}" style="height: 60px; width: 60px; object-fit: cover; border-radius: 6px;" />', obj.profile_image.url)
		return "No image"
	
	@admin.display(description="Image")
	def identity_document_preview(self, obj):
		print("print image url", obj.identity_document.url)
		if obj.identity_document:
			return format_html('<img src="{}" style="height: 60px; width: 60px; object-fit: cover; border-radius: 6px;" />', obj.identity_document.url)
		return "No image"

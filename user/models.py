from django.db import models
from django.core.files.storage import storages

from mysite.settings import get_private_storage, get_public_storage

class UserProfile(models.Model):
	name = models.CharField(max_length=255)
	age = models.PositiveIntegerField()
	profile_image = models.ImageField(upload_to="profiles/", storage=get_public_storage(), null=True)
	identity_document = models.ImageField(upload_to="identity/", storage=get_private_storage(), null=True)

	def __str__(self):
		return self.name

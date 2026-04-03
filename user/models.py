from django.db import models
from django.core.files.storage import storages

public_storage = storages["public"]
private_storage = storages["private"]

class UserProfile(models.Model):
	name = models.CharField(max_length=255)
	age = models.PositiveIntegerField()
	profile_image = models.ImageField(upload_to="profiles/", storage=public_storage, null=True)
	identity_document = models.ImageField(upload_to="identity/", storage=private_storage, null=True)

	def __str__(self):
		return self.name

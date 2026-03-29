from django.db import models

class UserProfile(models.Model):
	name = models.CharField(max_length=255)
	age = models.PositiveIntegerField()
	profile_image = models.ImageField(upload_to="profiles/")

	def __str__(self):
		return self.name

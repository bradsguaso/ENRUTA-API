from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to="image_profile", blank=True, null=True)
    photo_URL = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.username


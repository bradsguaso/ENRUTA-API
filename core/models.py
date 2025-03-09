from django.conf import settings
from django.db import models


# Create your models here.

class Charge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='charges', null=True)

    def __str__(self):
        return self.name

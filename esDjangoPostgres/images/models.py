from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=70, blank=False, default="")
    image_url = models.TextField(blank=False, default="")
    description = models.CharField(max_length=200, blank=False, default="")

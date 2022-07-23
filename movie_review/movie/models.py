from email.mime import image
from urllib.parse import urlsplit
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    image = models.ImageField(upload_to = 'movie/images/')
    url = models.URLField(blank=True)
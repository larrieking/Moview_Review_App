from ast import mod
from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='movie/images/')
    description = models.TextField(max_length=5000)
    created_date = models.DateTimeField(auto_now=True)
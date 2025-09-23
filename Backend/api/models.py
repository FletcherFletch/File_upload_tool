from django.db import models
from django.db.models import ImageField, FileField

# Create your models here.

class uupload(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name
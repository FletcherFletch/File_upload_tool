from django.db import models
from django.db.models import ImageField, FileField

# Create your models here.

class uupload(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #pic = models.ImageField(upload_to='PostPics/')
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE) 

class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
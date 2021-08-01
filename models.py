from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):

    cover = models.ImageField(upload_to='books/', blank=True, null=True)
    level = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    urllink = models.URLField(max_length=200)
    about = models.TextField(null=True, default='')
    liked_users = models.ManyToManyField(User, related_name='liked_books')

    def __str__(self):  
        return f'{self.level} : {self.title} : {self.author}'


class Video(models.Model):

    cover = models.ImageField(upload_to='videos/', blank=True, null=True)
    level = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    urllink = models.URLField(max_length=200)
    about = models.TextField(null=True, default='')
    who = models.TextField(null=True, default='')
    liked_users = models.ManyToManyField(User, related_name='liked_videos')

    def __str__(self): #해당 인스턴스가 어떤 attribute 가지고 있는지 간단하게 
        return f'{self.level} : {self.title}'


class Website(models.Model):

    cover = models.ImageField(upload_to='websites/', blank=True, null=True)
    level = models.CharField(max_length=10, default='')
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    urllink = models.URLField(max_length=200)
    about = models.TextField(null=True, default='')
    liked_users = models.ManyToManyField(User, related_name='liked_websites')

    def __str__(self): #해당 인스턴스가 어떤 attribute 가지고 있는지 간단하게 
        return f'{self.level} : {self.category} : {self.title}'

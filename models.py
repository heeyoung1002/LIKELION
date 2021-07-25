from django.db import models

# Create your models here.

class Book(models.Model):

    cover = models.ImageField (upload_to='',default='')
    level = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    urllink = models.URLField(max_length=200)
    about = models.TextField(null=True, default='')

    def __str__(self):  
        return f'{self.level} : {self.title} : {self.author}'


class Video(models.Model):

    cover = models.ImageField (upload_to='',blank=True, null=True) #이부분 수정해야함
    level = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    urllink = models.URLField(max_length=200)
    about = models.TextField(null=True, default='')
    who = models.TextField(null=True, default='')

    def __str__(self): #해당 인스턴스가 어떤 attribute 가지고 있는지 간단하게 
        return f'{self.level} : {self.title}'


class Website(models.Model):

    cover = models.ImageField (upload_to='',blank=True, null=True) #이부분 수정해야함
    level = models.CharField(max_length=10, default='')
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    urllink = models.URLField(max_length=200)
    about = models.TextField(null=True, default='')

    def __str__(self): #해당 인스턴스가 어떤 attribute 가지고 있는지 간단하게 
        return f'{self.level} : {self.category} : {self.title}'

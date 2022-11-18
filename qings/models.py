from django.db import models

# Create your models here.

class Poet(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/%y')
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.title


class Quote(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/%y')
    description = models.CharField(max_length=2000)


    def __str__(self):
        return self.title
    

class Video(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='video/%y')
    description = models.CharField(max_length=2000)


    def __str__(self):
        return self.title
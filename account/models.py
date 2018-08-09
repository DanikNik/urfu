from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.name + ' ' + self.surname

class Event(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
# Create your models here.

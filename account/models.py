from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class User(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' ' + self.surname

# Create your models here.

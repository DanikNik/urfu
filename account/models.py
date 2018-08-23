from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' ' + self.surname



class Event(models.Model):
    title = models.CharField(max_length=200)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.title


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


# Create your models here.

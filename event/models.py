from django.db import models
from account.models import Person

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200)
    members = models.ManyToManyField(Person, through='Membership')

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


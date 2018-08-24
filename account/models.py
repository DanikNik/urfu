from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    events = models.ManyToManyField('event.Event', through='event.Membership')

    class Meta:
        ordering = ["name"]

    def get_event_list(self):
        pass

    def __str__(self):
        return self.name + ' ' + self.surname

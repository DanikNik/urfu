from django.db import models
import uuid
from django.contrib.auth.models import User

class Person(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL)
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

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Person(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    projects = models.ManyToManyField('event.Project', through='event.ProjectMembership')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name + ' ' + self.surname

    def get_absolute_url(self):
        return reverse('person_detail', args=[self.id])
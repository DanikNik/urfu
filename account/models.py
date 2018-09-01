from django.db import models
from django.contrib.auth.models import User
# from authenticate.models import User
from django.urls import reverse
import uuid

class Person(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    # last_name = models.CharField(max_length=200, blank=True)

    avatar = models.ImageField(null=True)

    place_of_study = models.CharField(max_length=200, blank=True)
    group_number = models.CharField(max_length=20, blank=True)
    place_of_work = models.CharField(max_length=200, blank=True)
    job_position = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True)
    vk_link = models.URLField(blank=True)
    fb_link = models.URLField(blank=True)
    google_link = models.URLField(blank=True)
    tg_link = models.URLField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    type = models.CharField(max_length=200)
    projects = models.ManyToManyField('event.Project', through='event.ProjectMembership')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name + ' ' + self.surname

    def get_absolute_url(self):
        return reverse('person_detail', args=[self.id])
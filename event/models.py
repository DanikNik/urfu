from django.db import models
from django.contrib.auth.models import User
from account.models import Person
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    icon = models.ImageField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    is_visible = models.BooleanField(default=0)

    created_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    created_at_time = models.DateTimeField(null=True, blank=True)

    members = models.ManyToManyField(Person, through='ProjectMembership')

    class Meta:
        ordering = ["start_time"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', args=[self.id])


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    is_required = models.BooleanField(default=0)

    created_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    created_at_time = models.DateTimeField(null=True, blank=True)

    owner = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='owned_events', null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    members = models.ManyToManyField(Person, through='EventMembership')

    class Meta:
        ordering = ["start_time"]

    def __str__(self):
        return self.title + ' ' + '({})'.format('reqired' if self.is_required else 'not required')

    def get_absolute_url(self):
        return reverse('event_detail', args=[self.id])


class ProjectMembership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.person) + ' / ' + str(self.project)

    @classmethod
    def add_member(self, _person, _project):
        membership = self.objects.create(person=_person, project=_project)
        return membership


class EventMembership(models.Model):
    person = models.ForeignKey('account.Person', on_delete=models.CASCADE, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    project_membership = models.ForeignKey(ProjectMembership, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.person) + ' / ' + str(self.event)

    @classmethod
    def add_member(self, _person, _event, _project_membership):
        membership = self.objects.create(person=_person, event=_event, project_membership=_project_membership)
        return membership

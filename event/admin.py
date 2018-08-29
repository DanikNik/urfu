from django.contrib import admin
from .models import Project, Event, ProjectMembership, EventMembership

# Register your models here.
admin.site.register(Project)
admin.site.register(Event)
admin.site.register(ProjectMembership)
admin.site.register(EventMembership)
from django.contrib import admin
from . import models


class EventFilesInline(admin.TabularInline):
    model = models.EventFile
    extra = 1


class EventMembersInline(admin.TabularInline):
    model = models.EventMembership
    extra = 1


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    model = models.Event
    inlines = [EventFilesInline, EventMembersInline]


class ProjectFileInline(admin.TabularInline):
    model = models.ProjectFile
    extra = 1


class ProjectMembersInline(admin.TabularInline):
    model = models.ProjectMembership
    extra = 1


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    model = models.Project
    inlines = [ProjectFileInline, ProjectMembersInline]

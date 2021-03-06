from django.urls import reverse
from .models import Project, Event, ProjectMembership, EventMembership
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django import forms
from assets.forms.SubmitButton import SubmitButtonField
from assets.checks.user_check_mixins import ProfileCheckMixin


class RegisterButtonForm(forms.Form):
    field = SubmitButtonField(initial="REGISTER", label='')


class LeaveButtonForm(forms.Form):
    field = SubmitButtonField(initial="Leave", label='')


class ProjectListView(ProfileCheckMixin, ListView):
    model = Project
    context_object_name = "project_list"
    template_name = 'project/project_list.html'


class ProjectDetailView(ProfileCheckMixin, DetailView, FormMixin):
    model = Project
    context_object_name = 'project'
    template_name = 'project/project_detail.html'

    form_class = forms.Form

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        user_person = self.request.user.person
        if user_person not in self.object.members.all():
            project_membership = ProjectMembership.add_member(user_person, self.object)
            for event in self.object.event_set.all():
                if event.is_required:
                    event_membership = EventMembership.add_member(user_person, event, project_membership)
                    event_membership.save()
            project_membership.save()
            return super(ProjectDetailView, self).form_valid(form)
        else:
            membership_to_delete = ProjectMembership.objects.get(person=user_person, project=self.object)
            membership_to_delete.delete()
            return super(ProjectDetailView, self).form_valid(form)


class EventDetailView(ProfileCheckMixin, DetailView, FormMixin):
    model = Event
    context_object_name = "event"
    template_name = "project/event_detail.html"

    form_class = forms.Form

    def get_success_url(self):
        return reverse('event_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        user_person = self.request.user.person
        if user_person not in self.object.members.all():
            membership = EventMembership.add_member(user_person,
                                                    self.object,
                                                    ProjectMembership.objects.get(person=user_person,
                                                                                  project=self.object.project))
            membership.save()
            return super(EventDetailView, self).form_valid(form)
        else:
            membership_to_delete = EventMembership.objects.get(person=user_person, event=self.object)
            membership_to_delete.delete()
            return super(EventDetailView, self).form_valid(form)
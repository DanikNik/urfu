from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from assets.checks.user_check_mixins import StaffCheckMixin
from event.models import Project, Event
from django.utils import timezone


class CockpitIndexView(TemplateView):
    pass #TODO: add cockpit interface (list of possible operations)

class ProjectCreateView(StaffCheckMixin, CreateView):
    model = Project
    template_name = 'cockpit/project_create.html'

    fields = [
        'title',
        'description',
        'icon',
        'start_time',
        'end_time',
        'is_visible'
    ]

    def form_valid(self, form):
        project = form.save(commit=False)
        project.created_by = self.request.user
        project.created_at_time = timezone.now()
        project.save()
        return super(ProjectCreateView, self).form_valid(form)
#
class EventCreateView(StaffCheckMixin, CreateView):
    model = Event
    template_name = 'cockpit/event_create.html'

    fields =[
    'title',
    'description',
    'start_time',
    'end_time',
    'is_required',
    'owner',
    'project'
    ]

    def form_valid(self, form):
        event = form.save(commit=False)
        event.created_by = self.request.user
        event.created_at_time = timezone.now()
        event.save()
        return super(EventCreateView, self).form_valid(form)
from django.template import loader
from django.http import HttpResponse
from .models import Event
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
# Create your views here.

#TODO: перевести все views на class-based

class EventListView(ListView):
    model = Event
    template_name = 'event/event_list.html'
    context_object_name = "event_list"

class EventDetailView(FormMixin, DetailView):
    success_url = event
    pass



@login_required
def index(request):
    event_list = Event.objects.all()
    template = loader.get_template('event/index.html')
    context = {
        'event_list': event_list
    }
    return HttpResponse(template.render(context, request))


@login_required
def event(request, event_id):
    event = Event.objects.get(id=event_id)
    user_list = event.members.all()
    template = loader.get_template('event/event.html')
    context = {
        'event_title': Event.objects.get(id=event_id),
        'user_list': user_list
    }
    return HttpResponse(template.render(context, request))

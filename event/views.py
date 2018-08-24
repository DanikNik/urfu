from django.shortcuts import render
from django.views.generic import ListView
from django.template import loader
from django.http import HttpResponse
from .models import Event

# Create your views here.

def index(request):
    event_list = Event.objects.all()
    template = loader.get_template('event/index.html')
    context = {
        'event_list': event_list
    }
    return HttpResponse(template.render(context, request))

def event(request, event_id):
    event = Event.objects.get(id=event_id)
    user_list = event.members.all()
    template = loader.get_template('event/event.html')
    context = {
        'event_title': Event.objects.get(id=event_id),
        'user_list': user_list
    }
    return HttpResponse(template.render(context, request))

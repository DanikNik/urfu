from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Person, Event

def index(request):
    event_list= Event.objects.all()
    template = loader.get_template('account/index.html')
    context = {
        'event_list': event_list,

    }
    return HttpResponse(template.render(context, request))

def user(request, user_id):
    return HttpResponse(Person.objects.get(id=user_id))

def event(request, event_id):
    event = Event.objects.get(id=event_id)
    user_list = event.members.all()
    template = loader.get_template('account/event.html')
    context = {
        'event_title': Event.objects.get(id=event_id),
        'user_list': user_list
    }
    return HttpResponse(template.render(context, request))

# Create your views here.

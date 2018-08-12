from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import User, Event

def index(request):
    list= Event.objects.all()
    template = loader.get_template('index.html')
    context = {
        'list': list,
    }
    return HttpResponse(template.render(context, request))

def user(request, user_id):
    return HttpResponse(User.objects.get(id=user_id))

def event(request, event_id):
    return HttpResponse(Event.objects.get(id=event_id))

# Create your views here.

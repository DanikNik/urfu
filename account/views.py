from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Event

def index(request):
    query_set = User.objects.all()
    response = ''
    for i in query_set:
        response +='<p>' + str(i) + '\t' + '</p>'
    return HttpResponse(response)

def user(request, user_id):
    return HttpResponse(User.objects.get(id=user_id))

def event(request, event_id):
    return HttpResponse(Event.objects.get(id=event_id))

# Create your views here.

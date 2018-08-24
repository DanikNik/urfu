from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Person

def index(request):
    person_list= Person.objects.all()
    template = loader.get_template('account/index.html')
    context = {
        'person_list': person_list,

    }
    return HttpResponse(template.render(context, request))

def user(request, user_id):
    person = Person.objects.get(id=user_id)
    template = loader.get_template('account/user.html')
    context = {
        'user_name': person,
        'event_list': person.events.all()
    }
    return HttpResponse(template.render(context, request))

# Create your views here.

from django.shortcuts import render
from django.template import loader
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Person

class PersonListView(ListView):
    model = Person
    template_name = 'account/person_list.html'
    context_object_name = 'person_list'

# Create your views here.


class PersonDetailView(DetailView):
    model = Person
    template_name = 'account/person_detail.html'
    context_object_name = 'person'
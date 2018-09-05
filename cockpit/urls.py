from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.CockpitIndexView.as_view(), name="cockpit"),
    path('add_project/', login_required(views.ProjectCreateView.as_view()), name='project_create'),
    path('add_event/', login_required(views.EventCreateView.as_view()), name='event_create')
]

from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', login_required(views.ProjectListView.as_view()), name='project_list'),
    path('project/<pk>', login_required(views.ProjectDetailView.as_view()), name='project_detail'),
    path('event/<pk>', login_required(views.EventDetailView.as_view()), name='event_detail')
]

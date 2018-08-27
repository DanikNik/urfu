from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', login_required(views.EventListView.as_view()), name='event_list'),
    path('<int:pk>/', login_required(views.EventDetailView.as_view()), name='event_detail'),
]

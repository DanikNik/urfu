from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:user_id>/', views.user, name='user'),
    path('event/<int:event_id>/', views.event, name='event')
]

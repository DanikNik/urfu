from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:event_id>/', views.event, name='event'),
    # path('event/<int:event_id>/', views.event, name='event')
]

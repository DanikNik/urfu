from django.urls import path


from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project_list'),
    path('<pk>', views.ProjectDetailView.as_view(), name='project_detail'),
    path('event/<pk>', views.EventDetailView.as_view(), name='event_detail')
]

from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.RegisterFormView.as_view()),
    path('new_person/<int:user_id>/', views.NewPersonView.as_view()),
    path('login/', views.LoginFormView.as_view()),
]
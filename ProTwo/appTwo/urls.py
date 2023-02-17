from django.urls import path
from appTwo import views

urlpatterns = [
    path('', views.users, name='users')
]
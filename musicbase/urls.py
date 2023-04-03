from django.urls import path
from .import views

urlpatterns = [
    path ('', views.topsong, name='home'),
]
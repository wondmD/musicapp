from django.urls import path
from .import views

urlpatterns = [
    path ('', views.topsong, name='topsong'),
    path ('', views.home, name='home'),
]
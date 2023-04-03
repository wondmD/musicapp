from django.shortcuts import render
from django.http import HttpResponse
from .models import music
from django.template import loader
# Create your views here.

def home(request):
    return HttpResponse("hello my page")

def topsong(request):
    list_od_top_song = music.objects.order_by('-likes')[:6]
    template = loader.get_template ('musicbase/index.html')

    context = {
        'list_od_top_song' : list_od_top_song
    }
    return HttpResponse(template.render(context, request))
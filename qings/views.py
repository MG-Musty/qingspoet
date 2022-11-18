from django.shortcuts import render
from django.template import loader
from .models import Poet, Quote, Video
from django.http import Http404

from . import views
# Create your views here.

def index(request):
    return render(request, "qings/index.html")

def poets(request):
    poets = Poet.objects.all()
    if poets is not None:
        return render(request, "qings/poets.html", {"poets": poets})
    else:
        raise Http404('Image not display!')

def about(request):
    return render(request, "qings/about.html")

def quotes(request):
    quotes = Quote.objects.all()
    if quotes is not None:
        return render(request, "qings/quotes.html", {"quotes": quotes})
    else:
        raise Http404('Not accepted!')
    
def videos(request):
    videos = Video.objects.all()
    if videos is not None:
        return render(request, "qings/videos.html", {"videos": videos})
    else:
        raise Http404('No video!')

def contacts(request):
    return render(request, "qings/contacts.html")

from django.shortcuts import render
from django.template import loader
from .models import Poet, Quote, Video, Contact, Blog
from django.http import Http404, HttpResponse

from django.views import generic

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
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.message=message
        contact.save()
        return HttpResponse("<h3 text-center>THANKS FOR CONTACTING US!</H3>")
    return render(request, "qings/contacts.html")


class BlogList(generic.ListView):
    queryset = Blog.objects.filter(status=1).order_by('-created_on')
    template_name = 'qings/blogs.html'

class Detail(generic.DetailView):
    model = Blog
    template_name = 'qings/details.html'

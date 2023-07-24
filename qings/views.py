from django.shortcuts import render
from django.template import loader
from .models import Poet, Quote, Video, Contact, Blog
from django.http import Http404, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

from django.views import generic
#contact us page
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from qings.forms import ContactUsForm

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
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "qings/contacts.html")
 

class BlogList(generic.ListView):
    queryset = Blog.objects.filter(status=1).order_by('-created_on')
    template_name = 'qings/blogs.html'

class Detail(generic.DetailView):
    model = Blog
    template_name = 'qings/details.html'



""""def contacts(request):
    if request.method == 'POST':
        # create an instance of our form, and fill it with the POST data
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonymous"} via Qingspoet Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@qingspoet.xyz'],
            )
            return HttpResponseRedirect('/email_sent/')
        # if the form is not valid, we let execution continue to the return
        # statement below, and display the form again (with errors).

    else:
        # this must be a GET request, so create an empty form
        form = ContactUsForm()

    return render(request,
                  'qings/contacts.html',
                  {'form': form})

def email_sent(request):
    return render(request, 'qings/email_sent.html') """
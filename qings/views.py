from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def index(request):
    return render(request, "qings/index.html")

def poets(request):
    return render(request, "qings/poets.html")

def about(request):
    return render(request, "qings/about.html")

def quotes(request):
    return render(request, "qings/quotes.html")

def contacts(request):
    return render(request, "qings/contacts.html")
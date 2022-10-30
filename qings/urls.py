from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = staticfiles_urlpatterns()

urlpatterns = [
    path("", views.index, name="index"),
    path("poets", views.poets, name="poets"),
    path("about", views.about, name="about"),
    path("quotes", views.quotes, name="quotes"),
    path("contacts", views.contacts, name="contacts"),
]
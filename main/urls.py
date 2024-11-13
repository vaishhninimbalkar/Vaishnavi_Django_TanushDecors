from django.contrib import admin
from django.urls import include, path

from tanushdecors import views

urlpatterns = [
    path('',        views.redirect_to_home, name='home'),
    path('polls/',  include('polls.urls')),
    path('admin/',  admin.site.urls)
]


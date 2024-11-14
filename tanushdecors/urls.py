"""
"""
from django.urls import path

from . import views
from django.conf.urls import handler404, handler500

app_name = 'tanushdecors'
urlpatterns = [
    path('',           views.IndexView.as_view(), name='index'),
    path('vaishnavi/', views.VaishnaviView.as_view(), name='home_vaishnavi'),
]

from django.contrib import admin
from django.urls import include, path

from polls import views as p_views
from tanushdecors import views as t_views

urlpatterns = [
    path('',        p_views.redirect_to_home, name='home'),
    path('polls/',  include('polls.urls')),
    
    path('tanushdecors/',  include('tanushdecors.urls')),

    path('admin/',  admin.site.urls),
]


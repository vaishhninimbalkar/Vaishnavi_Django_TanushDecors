from django.contrib import admin
from django.urls import include, path

from polls        import views as p_views
from tanushdecors import views as t_views

urlpatterns = [
    path('',        p_views.redirect_to_home, name='home'),

    # This is our Polls App
    path('polls/',  include('polls.urls')),
    
    # This is our Tanush Decors app
    path('tanushdecors/',  include('tanushdecors.urls')),

    # This is the Django Admin Page
    path('admin/',  admin.site.urls),
]


from django.contrib import admin

from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from tanushdecors import views as t_views

urlpatterns = [
    # This is our Tanush Decors app
    path('',  include('tanushdecors.urls')),

    # This is the Django Admin Page
    path('admin/',  admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

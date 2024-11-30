from django.contrib import admin

from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import TemplateView 

urlpatterns = [
    path('',  include('tanushdecors.urls')),

    path('admin/',  admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    
    path("accounts/home", TemplateView.as_view(template_name="home.html"), name="home"),  # new
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

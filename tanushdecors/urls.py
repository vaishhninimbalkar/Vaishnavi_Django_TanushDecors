from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'tanushdecors'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('vaishnavi/', views.VaishnaviView.as_view(), name='home_vaishnavi'),
    path('products/', views.product_list, name='product_list'),
]

# Add this for serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

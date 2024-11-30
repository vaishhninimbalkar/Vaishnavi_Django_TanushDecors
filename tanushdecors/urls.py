from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'tanushdecors'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('products/', views.product_list, name='product_list'),
    path('shop/', views.shop, name='shop'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
         
    path('thankyou/', views.thankyou, name='thankyou'),
    path('login/', views.login, name='login'),
]

# Add this for serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


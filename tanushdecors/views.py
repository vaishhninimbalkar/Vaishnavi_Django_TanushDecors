# -*- coding: utf-8 -*-

import logging
from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Product

# Initialize the logger for the app
LOGGER = logging.getLogger('tanushdecors')


class IndexView(generic.ListView):
    """
    IndexView: Displays the latest products.
    """
    template_name = 'tanushdecors/index.html'
    context_object_name = 'latest_product_list'

    LOGGER.debug('Initializing IndexView')

    def get_queryset(self):
        """
        Fetches the latest 5 products published before or at the current time, ordered by publication date.
        """
        return Product.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

def product_list(request):
    products = Product.objects.all()
    return render(request, 'tanushdecors/products.html', {'products': products})

def shop(request):
    products = Product.objects.all()
    return render(request, 'tanushdecors/shop.html', {'products': products})

def about(request):
    return render(request, 'tanushdecors/about.html')

def services(request):
    return render(request, 'tanushdecors/services.html')

def blog(request):
    return render(request, 'tanushdecors/blog.html')

def contact(request):
    return render(request, 'tanushdecors/contact.html')

def cart(request):
    return render(request, 'tanushdecors/cart.html')

def thankyou(request):
    return render(request, 'tanushdecors/thankyou.html')

def login(request):
    return render(request, 'tanushdecors/login.html')
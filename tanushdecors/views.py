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


class VaishnaviView(generic.TemplateView):
    """
    VaishnaviView: A placeholder view for the 'vaishnavi.html' page.
    """
    template_name = 'tanushdecors/vaishnavi.html'

    LOGGER.debug('Initializing VaishnaviView')

    def get_context_data(self, **kwargs):
        """
        Provides an optional context for the Vaishnavi view.
        """
        context = super().get_context_data(**kwargs)
        context['message'] = 'Welcome to Vaishnavi\'s custom view!'
        return context


def product_list(request):
    """
    Function-based view for displaying all products.
    """
    LOGGER.debug('Fetching all products for product_list view')
    products = Product.objects.all()
    return render(request, 'tanushdecors/products.html', {'products': products})

def shop(request):
    products = Product.objects.all()
    return render(request, 'tanushdecors/shop.html', {'products': products})

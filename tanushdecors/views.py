# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.views import generic
from django.utils import timezone

from .models import Product


class IndexView(generic.ListView):
    """
    IndexView:
    """
    template_name = 'tanushdecors/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Product.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class VaishnaviView(generic.ListView):
    template_name = 'tanushdecors/vaishnavi.html'

    def get_queryset(self):
        return None

def product_list(request):
    products = Product.objects.all()
    return render(request, 'tanushdecors/products.html', {'products': products})

# -*- coding: utf-8 -*-

import logging

from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Products

LOGGER = logging.getLogger('tanushdecors')


class IndexView(generic.ListView):
    """
    IndexView:
    """
    template_name = 'tanushdecors/index.html'
    context_object_name = 'latest_question_list'

    LOGGER.debug('IndexView |')

    def get_queryset(self):
        return Products.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class VaishnaviView(generic.ListView):
    template_name = 'tanushdecors/vaishnavi.html'

    def get_queryset(self):
        return None

def redirect_to_vaishnavi(request):
    return HttpResponse("Hello, i am Vaishnavi")

# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect  # HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

class IndexView(generic.ListView):
    """
    IndexView:
    """
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """DetailView"""

    data = {}

    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    """
    ResultsView:
    """
    
    data = {}

    model = Question
    template_name = 'polls/results.html'

class ResultsOverviewView(generic.ListView):
    template_name = 'polls/results-overview.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')


class HelpView(generic.ListView):
    """
    HelpView:
    """
    template_name = 'polls/help.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

def index(request):
    """
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    question = get_object_or_404(Question, pk=question_id)
    data = {'question': question}

    return render(request, 'polls/detail.html', data)


def results(request):
    """
    results:
    """

    data = { 'mode': 'full'}

    return render(request, 'polls/results.html', data)


def vote(request, question_id):
    """
    vote:
    """

    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice. ID was %d" % question_id,
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



def help(request):
    """
    """
    
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    return render(request, 'polls/help.html', context)


def error404(request, exception):
    data = {}
    return render(request,'polls/error/404.html', data)


def error500(request, exception):
    data = {}
    return render(request,'polls/error/500.html', data)

def redirect_to_home(request):
    return redirect('/polls')
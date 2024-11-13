"""
"""
from django.urls import path

from . import views
from django.conf.urls import handler404, handler500

app_name = 'polls'
urlpatterns = [
    path('',                        views.IndexView.as_view(),              name='index'),
    path('<int:pk>/',               views.DetailView.as_view(),             name='detail'),
    path('<int:pk>/results/',       views.ResultsView.as_view(),            name='results'),
    path('<int:question_id>/vote/', views.vote,                             name='vote'),
    path('results/',                views.ResultsOverviewView.as_view(),    name='result-overview'),
    path('help/',                   views.HelpView.as_view(),               name='help')
]

#handler404 = views.error404
#handler500 = views.error500

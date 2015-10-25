# coding: utf-8
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.MainView.as_view(), name='main'),
    url(r'^(?P<screen>\d+)/page/(?P<page>\d+)', views.PageView.as_view(), name='page'),
)

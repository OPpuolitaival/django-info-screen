# coding: utf-8
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^api/', views.ScreenJsonView.as_view(), name='api'),
    url(r'^(?P<screen>\d+)/', views.ScreenView.as_view(), name='screen'),
    url(r'^image/(?P<page>\d+)', views.ImageView.as_view(), name='image'),
)

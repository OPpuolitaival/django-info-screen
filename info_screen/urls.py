# coding: utf-8
from django.conf.urls import url

from . import views

app_name = 'info_screen'

urlpatterns = [
    url(r'^api/', views.ScreenJsonView.as_view(), name='api'),
    url(r'^image/(?P<page_uuid>.*)', views.ImageView.as_view(), name='image'),
    url(r'^(?P<screen_uuid>.*)/', views.ScreenView.as_view(), name='screen'),
]

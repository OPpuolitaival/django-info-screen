# coding: utf-8
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^info_screen/', include('info_screen.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

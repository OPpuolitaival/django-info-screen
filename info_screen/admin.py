# coding: utf-8
from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import InfoScreen, Page

admin.site.register(InfoScreen)
admin.site.register(Page)


class MyAdminSite(AdminSite):
    site_header = 'Info screen admin site'


admin_site = MyAdminSite(name='info screen admin')
admin_site.register(InfoScreen)
admin_site.register(Page)

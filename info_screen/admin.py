# coding: utf-8
from django.contrib import admin

from .models import InfoScreen, Page


class PageAdmin(admin.ModelAdmin):
    """
    MyWorkTurnAdmin
    """
    fields = ('timestamp', 'last_edit', 'title', 'continuous', 'start', 'end', 'order',
              'type', 'url', 'image_file', 'uuid', 'delay_in_sec', 'is_slideshow_page')
    readonly_fields = ('timestamp', 'last_edit', 'uuid')
    list_display = ('title', 'delay_in_sec', 'continuous', 'start', 'end', 'type', 'uuid')
    list_filter = ('continuous', 'type')  # Right side filter
    ordering = ('timestamp',)


class InfoScreenAdmin(admin.ModelAdmin):
    """
    MyWorkTurnAdmin
    """
    fields = ('uuid', 'timestamp', 'last_edit', 'title', 'delay_in_sec', 'pages')
    readonly_fields = ('uuid', 'timestamp', 'last_edit')
    list_display = ('title', 'delay_in_sec', 'timestamp', 'uuid')
    ordering = ('title',)
    filter_horizontal = ('pages',)  # Better view for M2M fields

admin.site.register(InfoScreen, InfoScreenAdmin)
admin.site.register(Page, PageAdmin)

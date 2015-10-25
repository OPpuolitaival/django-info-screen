# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Page(models.Model):
    """
    One view
    """
    timestamp = models.DateTimeField(_('Added'), auto_now_add=True, db_index=True)
    last_edit = models.DateTimeField(_('Last time edited'), auto_now=True, null=True)
    # Readonly if integrated system make some default views
    readonly = models.BooleanField(_('readonly'), default=False)
    title = models.CharField(_('Title'), max_length=255, default='')
    # Permanent page
    continuous = models.BooleanField(_('Continuous'), default=False)
    # Set creation time if not defined
    start = models.DateTimeField(_('view starting time'), db_index=True, null=True, blank=True)
    # If not defined, then visible for ever'
    end = models.DateTimeField(_('view ending time'), db_index=True, null=True, blank=True)
    IFRAME = 0
    IMAGE = 1
    VIEW_TYPE = (
        (IFRAME, _('iframe')),
        (IMAGE, _('image')),
    )
    type = models.PositiveIntegerField(_('view type'), choices=VIEW_TYPE, default=IMAGE, db_index=True)
    url = models.URLField(_('url'), blank=True, null=True)
    image_file = models.FileField(_('image file'), upload_to='info_view/%Y/%m/%d', null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        app_label = 'info_screen'
        ordering = ['start']
        verbose_name = _("Page")
        verbose_name_plural = _("Page")


class BackLink(models.Model):
    """
    Back link is useful when integrating to another system and need to make visible how to user get back to the main
    system
    """
    link = models.URLField(_('link'))
    link_text = models.CharField(_('Link text'), max_length=255)

    def __unicode__(self):
        return self.link

    class Meta:
        app_label = 'info_screen'
        ordering = ['link_text']
        verbose_name = _("Back link")
        verbose_name_plural = _("Back links")


class InfoScreen(models.Model):
    """
    InfoScreen which collects a set of views to show in loop
    """
    timestamp = models.DateTimeField(_('Added'), auto_now_add=True, db_index=True)
    last_edit = models.DateTimeField(_('Last time edited'), auto_now=True, null=True)
    delay_in_sec = models.IntegerField(_('Delay in seconds'), default=5)

    title = models.CharField(_('Title'), max_length=255, default='', null=True)
    pages = models.ManyToManyField(Page, verbose_name=_('InfoScreen'), blank=True)
    back_link = models.ForeignKey(BackLink, null=True, blank=True, verbose_name=_('Back link'))
    # People that can make changes to this info screen
    owners = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_('Users'), blank=True)

    def __str__(self):
        return u"{}".format(self.title)

    class Meta:
        app_label = 'info_screen'
        ordering = ['timestamp']
        verbose_name = _("InfoScreen")
        verbose_name_plural = _("InfoScreen")

# coding: utf-8
import uuid

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Page(models.Model):
    """
    One view
    """
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
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
    # Order integer, smallest numbers shown first
    order = models.IntegerField(_('order'), db_index=True, default=0)
    delay_in_sec = models.IntegerField(_('Default delay in seconds'), default=5)
    URL = 0
    IMAGE = 1
    VIEW_TYPE = (
        (URL, _('url')),
        (IMAGE, _('image')),
    )
    type = models.PositiveIntegerField(_('view type'), choices=VIEW_TYPE, default=IMAGE, db_index=True)
    url = models.URLField(_('url'), blank=True, null=True)
    image_file = models.FileField(_('image file'), upload_to='info_view/%Y/%m/%d', null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        app_label = 'info_screen'
        ordering = ['order', 'start']
        verbose_name = _("Page")
        verbose_name_plural = _("Page")

    def next_page(self, screen):
        queryset = screen.visible_pages()

        # in case that there is no pages
        if not queryset.exists():
            return None

        # Query if there are some left in this round
        queryset_next = queryset.filter(pk__gt=self.pk)

        if queryset_next.count() > 0:
            # If not latest one
            next_page = queryset_next[0]
        else:
            # If the page is latest one
            next_page = queryset[0]
        return next_page

    def show_url(self):
        if self.type == Page.IMAGE:
            url = reverse('info_screen:image', kwargs={'page_uuid': self.uuid})
        elif self.type == Page.URL:
            url = self.url
        else:
            url = None
        return url


class InfoScreen(models.Model):
    """
    InfoScreen which collects a set of views to show in loop
    """
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    timestamp = models.DateTimeField(_('Added'), auto_now_add=True, db_index=True)
    last_edit = models.DateTimeField(_('Last time edited'), auto_now=True, null=True)
    delay_in_sec = models.IntegerField(_('Delay in seconds'), default=5)

    title = models.CharField(_('Title'), max_length=255, default='', null=True)
    pages = models.ManyToManyField(Page, verbose_name=_('InfoScreen'), blank=True)

    def visible_pages(self):
        queryset = Page.objects.filter(infoscreen=self).order_by('pk')
        queryset = queryset.filter(
                # Search visible pages at the moment
                Q(start__lt=timezone.now(), end__gt=timezone.now()) |
                # Continuous pages are shown anyway
                Q(continuous=True)
        )
        return queryset

    def __str__(self):
        return u"{}".format(self.title)

    class Meta:
        app_label = 'info_screen'
        ordering = ['timestamp']
        verbose_name = _("InfoScreen")
        verbose_name_plural = _("InfoScreen")

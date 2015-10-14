# coding: utf-8
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from .models import InfoScreen, Page
from django.utils import timezone
from django.db.models import Q


class PageView(TemplateView):
    template_name = 'info_screen/page.html'

    def get_context_data(self, **kwargs):
        """
        Excludes any polls that aren't published yet.
        """
        context = super(PageView, self).get_context_data(**kwargs)
        screen = get_object_or_404(InfoScreen, pk=kwargs['screen'])
        page = get_object_or_404(Page, pk=kwargs['page'])
        queryset = Page.objects.filter(infoscreen=screen).order_by('pk')
        queryset = queryset.filter(
            # Search visible pages at the moment
            Q(start__lt=timezone.now(), end__gt=timezone.now()) |
            # If end time is missing, then the page is visible forever
            Q(end=None)
        )

        # Query if there are some left in this round
        queryset_next = queryset.filter(pk__gt=page.pk)

        if queryset_next.count() > 0:
            # If not latest one
            next_page = queryset_next[0]
        else:
            # If the page is latest one
            next_page = queryset[0]

        context.update({
            'next_page': next_page,
            'page': page,
            'collection': screen
        })

        return context

# coding: utf-8
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from .models import Collection, Page
from django.utils import timezone


class PageView(TemplateView):
    template_name = 'info_screen/page.html'

    def get_context_data(self, **kwargs):
        """
        Excludes any polls that aren't published yet.
        """
        context = super(PageView, self).get_context_data(**kwargs)
        collection = get_object_or_404(Collection, pk=kwargs['collection'])
        page = get_object_or_404(Page, pk=kwargs['page'])

        queryset = Page.objects.filter(collection=collection).order_by('pk')
        queryset = queryset.filter(start__lt=timezone.now()).filter(end__gt=timezone.now())
        queryset_next = queryset.filter(pk__gt=page.pk)
        if queryset_next.count() > 0:
            next_page = queryset_next[0]
        else:
            next_page = queryset[0]

        context.update({
            'next_page': next_page,
            'page': page,
            'collection': collection
        })

        return context

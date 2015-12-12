# coding: utf-8
import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, View

from .models import InfoScreen, Page


class ScreenView(TemplateView):
    template_name = 'info_screen/screen.html'

    def get_context_data(self, **kwargs):
        """
        Excludes any polls that aren't published yet.
        """
        context = super(ScreenView, self).get_context_data(**kwargs)
        screen = get_object_or_404(InfoScreen, pk=kwargs['screen'])

        context.update({
            'page': screen.visible_pages().first(),
            'screen': screen,
        })

        return context


class ImageView(TemplateView):
    template_name = 'info_screen/image.html'

    def get_context_data(self, **kwargs):
        context = super(ImageView, self).get_context_data(**kwargs)
        page = get_object_or_404(Page, pk=kwargs['page'])

        context.update({
            'image_url': page.image_file.url,
        })

        return context


class ScreenJsonView(View):
    def get(self, *args, **kwargs):
        print self.request.GET
        ret = dict()
        keys = self.request.GET.keys()
        current_page = None
        np = None

        if 'page_id' in keys:
            page_id = self.request.GET['page_id']
            if page_id.isdigit():
                current_page = get_object_or_404(Page, pk=page_id)

        if 'screen_id' in keys:
            screen = get_object_or_404(InfoScreen, pk=self.request.GET['screen_id'])
            if current_page is not None:
                # Normal case
                np = current_page.next_page(screen)
            else:
                # Case that no page, i.e. no visible pages
                if screen.visible_pages().exists():
                    np = screen.visible_pages().first()

            if np:
                ret = {
                    'id': np.id,
                    'url': np.show_url(),
                    'delay_in_sec': screen.delay_in_sec}

        return HttpResponse(json.dumps(ret))

from django.shortcuts import render
from django.views.generic import TemplateView


class LivePriceView(TemplateView):
    template_name = 'live2.html'

    def get_context_data(self, **kwargs):
        from Users.Scrapper import get_ticker_list
        context = super().get_context_data(**kwargs)
        context['stocks'] = get_ticker_list()

        return context
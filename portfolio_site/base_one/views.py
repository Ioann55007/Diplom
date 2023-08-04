from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


def error_page(request):
    return render(request, '404.html')


class BaseView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class IndexTwo(TemplateView):
    template_name = "index-2.html"


class AboutView(TemplateView):
    template_name = "about.html"


class FlexSliderView(TemplateView):
    template_name = "index-3.html"


class YouVim(TemplateView):
    template_name = 'index-4.html'


class Hom_ParalView(TemplateView):
    template_name = 'index-5.html'


class NewsOneView(TemplateView):
    template_name = 'static_html/news-1.html'

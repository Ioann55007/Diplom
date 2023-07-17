from django.shortcuts import render
from django.views import View


def error_page(request):
    return render(request, '404.html')


class BaseView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)




class HeadView(View):
    template_name = 'static_html/header.html'

    def get(self, request):
        return render(request, self.template_name)


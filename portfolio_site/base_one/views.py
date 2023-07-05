from django.shortcuts import render


def error_page(request):
    return render(request, '404.html')

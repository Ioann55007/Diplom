from django.urls import path, include
from . import views


urlpatterns = [
    path('not_found/', views.error_page, name='error_page')
]

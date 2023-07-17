from django.urls import path, include
from . import views


urlpatterns = [
    path('not_found/', views.error_page, name='error_page'),
    path('', views.BaseView.as_view(), name='index'),
    path('header/', views.HeadView.as_view(), name='head'),
]

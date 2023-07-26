from django.urls import path, include
from . import views


urlpatterns = [
    path('not_found/', views.error_page, name='error_page'),
    path('', views.BaseView.as_view(), name='index'),
    path('index-carousel/', views.IndexTwo.as_view(), name='carousel'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('flex_slider', views.FlexSliderView.as_view(), name='flex_slider'),
    path('you-vim', views.YouVim.as_view(), name='you-vim'),
    path('hom-palal', views.Hom_ParalView.as_view(), name='hom-palal'),
    path('news-1', views.NewsOneView.as_view(), name='news-1'),
]

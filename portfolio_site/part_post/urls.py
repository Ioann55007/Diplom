from django.urls import path
from. import views

app_name = 'part_post'


urlpatterns = [
    path('news-1', views.NewsOneView.as_view(), name='news-1'),
    path('news_detail/<slug:slug>/', views.NewsDetail.as_view(), name='news-post'),
]
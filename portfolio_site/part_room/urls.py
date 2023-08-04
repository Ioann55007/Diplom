from django.urls import path
from django.views.generic import TemplateView
from . import views
app_name = 'part_room'

urlpatterns = [
    path('rooms-1/', TemplateView.as_view(template_name='room-list-1.html'), name='rooms_list_one'),
    path('rooms-2/', TemplateView.as_view(template_name='room-list-2.html'), name='rooms_list_two'),
    path('rooms-3/', TemplateView.as_view(template_name='room-list-3.html'), name='rooms_list_three'),

]

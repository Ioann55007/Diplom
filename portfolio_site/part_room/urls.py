from django.urls import path
from django.views.generic import TemplateView
from . import views
# from base_one.views import StripeWebhookView
app_name = 'part_room'

urlpatterns = [
    path('rooms-1/', views.RoomListView.as_view(), name='rooms_list_one'),
    path('rooms-2/', TemplateView.as_view(template_name='room-list-2.html'), name='rooms_list_two'),
    path('rooms-3/', TemplateView.as_view(template_name='room-list-3.html'), name='rooms_list_three'),
    path('room-detail/<int:pk>/', views.room_detail, name='room'),
    # path("webhooks/stripe/", StripeWebhookView.as_view(), name="stripe-webhook"),

    path('delete-review/<int:id>/', views.review_delete, name='delete_review'),
    path('review/<int:pk>/', views.review_room, name='review'),
    path("double_room/<int:pk>/", views.DoubleRoomDetailView.as_view(), name="double_room_detail"),
    path("deluxe_room/<int:pk>/", views.DeluxeRoomDetailView.as_view(), name="deluxe_room_detail"),
    path("superior_room/<int:pk>/", views.SuperiorDetailView.as_view(), name="superior_room_detail"),
]
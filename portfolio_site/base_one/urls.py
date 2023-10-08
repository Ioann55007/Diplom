from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('not_found/', views.error_page, name='error_page'),
    path('', views.BaseView.as_view(), name='index'),
    path('index-carousel/', views.IndexTwo.as_view(), name='carousel'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact-form/', views.ContactCreateView.as_view(), name='contact_form'),
    path("booking/", views.BookingListView.as_view(), name="booking"),
    path("restaurant-list/", views.RestaurantListView.as_view(), name="restaurants"),
    path("restaurant-detail/<slug:slug>/", views.RestaurantDetail.as_view(), name="restaurant"),
]

urlpatterns += [
    path(
        "create-checkout-session/<int:pk>/",
        views.CreateStripeCheckoutSessionView.as_view(),
        name="create-checkout-session"),
    path("success/", views.SuccessView.as_view(), name="success"),
    path("cancel/", views.CancelView.as_view(), name="cancel"),
    path("booking/<int:pk>/", views.BookingHotelDetailView.as_view(), name="booking_detail")
]
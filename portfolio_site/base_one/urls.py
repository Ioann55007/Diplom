from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('not_found/', views.error_page, name='error_page'),
    path('', views.BaseView.as_view(), name='index'),
    path('index-carousel/', views.IndexTwo.as_view(), name='carousel'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('flex_slider', views.FlexSliderView.as_view(), name='flex_slider'),
    path('you-vim', views.YouVim.as_view(), name='you-vim'),
    path('hom-palal', views.Hom_ParalView.as_view(), name='hom-palal'),
    # path('news-1', views.NewsOneView.as_view(), name='news-1'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contacts/', TemplateView.as_view(template_name='contacts.html'), name='contacts'),
    path('menu-2/', TemplateView.as_view(template_name='menu-2.html'), name='menu_2'),
    path('menu-3/', TemplateView.as_view(template_name='menu-3.html'), name='menu_3'),
    path('menu-4/', TemplateView.as_view(template_name='menu-4.html'), name='menu_4'),
    # path('contact-form/', views.contact_form, name='contact_form'),
    # path("booking/", views.Booking.as_view(), name="booking"),
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

    path("webhooks/stripe/", views.StripeWebhookView.as_view(), name="stripe-webhook"),
    path("booking/<int:pk>/", views.BookingHotelDetailView.as_view(), name="booking_detail")
]
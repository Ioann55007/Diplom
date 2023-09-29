from django.urls import path
from . import views
from .views import CreateStripeCheckoutSessionView, SuccessView, CancelView

urlpatterns = [
    # path('pay/', views.HomePageView.as_view(), name='pay_home'),]
    # path('config/', views.stripe_config),
    # path('create-checkout-session/', views.create_checkout_session),  # new
    path(
        "create-checkout-session/<int:pk>/",
        CreateStripeCheckoutSessionView.as_view(),
        name="create-checkout-session"),
    path("success/", SuccessView.as_view(), name="success"),
    path("cancel/", CancelView.as_view(), name="cancel"),
    path("pay_list/", views.ProductListView.as_view(), name="product-list"),
    path("<int:pk>/", views.ProductDetailView.as_view(), name="product-detail"),
    path("webhooks/stripe/", views.StripeWebhookView.as_view(), name="stripe-webhook"),
]

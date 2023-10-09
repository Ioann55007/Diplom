from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
import stripe
from django.conf import settings
from django.shortcuts import redirect
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .forms import ContactForm
from .models import BookingHotel, Restaurant

stripe.api_key = settings.STRIPE_SECRET_KEY


class RestaurantListView(ListView):
    template_name = 'static_html/restaurants.html'
    context_object_name = 'restaurants'
    model = Restaurant


class RestaurantDetail(DetailView):
    template_name = 'static_html/restaurant.html'
    model = Restaurant

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'restaurant'
        return context


def error_page(request):
    return render(request, '404.html')


class BaseView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class IndexTwo(TemplateView):
    template_name = "index-2.html"


class AboutView(TemplateView):
    template_name = 'about.html'


class BookingListView(ListView):
    model = BookingHotel
    context_object_name = "booking"
    template_name = "booking_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        booking = BookingHotel.objects.last()
        context['booking'] = booking
        return context


class BookingHotelDetailView(DetailView):
    model = BookingHotel
    context_object_name = "booking_in_hotel"
    template_name = "booking_detail.html"
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(BookingHotelDetailView, self).get_context_data()
        context["booking"] = BookingHotel.objects.get(id=self.kwargs["pk"])

        return context

    def form_valid(self, form):
        form.instance.date_reg = timezone.now()
        return super().form_valid(form)


class CreateStripeCheckoutSessionView(View):
    """
    Create a checkout session and redirect the user to Stripe's checkout page
    """

    def post(self, request, *args, **kwargs):
        booking = BookingHotel.objects.get(id=self.kwargs["pk"])
        booking_sum = booking.adults * booking.childs
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": int(booking_sum * booking.price) * 100,
                        "product_data": {
                            "name": booking.price,

                        },
                    },
                    "quantity": booking.quantity,
                }
            ],
            metadata={"product_id": booking.id},
            mode="payment",
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )
        return redirect(checkout_session.url)


class SuccessView(TemplateView):
    template_name = "success.html"


class AjaxMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        def is_ajax():
            return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

        request.is_ajax = is_ajax.__get__(request)
        response = self.get_response(request)
        return response


class Booking(TemplateView):
    template_name = 'booking_detail.html'


class CancelView(TemplateView):
    template_name = "cancel.html"


class ContactCreateView(CreateView):
    form_class = ContactForm
    template_name = 'contacts.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super().form_valid(form)

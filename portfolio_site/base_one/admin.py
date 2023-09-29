from django.contrib import admin
from .models import ReviewHotel, BookingHotel


@admin.register(ReviewHotel)
class AdminReviewHotel(admin.ModelAdmin):
    list_display = ('name_author', 'created', 'text_review')
    list_display_links = ('name_author',)


@admin.register(BookingHotel)
class AdminBookingHotel(admin.ModelAdmin):
    list_display = ('arrival_date', 'date_of_departure', 'room_booking', 'adults', 'childs')
    list_display_links = ('room_booking',)
from django.contrib import admin
from .models import BookingHotel, Restaurant, PhotoDishRestaurant


@admin.register(BookingHotel)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user_booking', 'arrival_date', 'date_of_departure', 'adults', 'childs', 'quantity', 'price')
    list_display_links = ('user_booking',)



@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'average_bill', 'description')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}



@admin.register(PhotoDishRestaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'add_photo')
    list_display_links = ('restaurant',)
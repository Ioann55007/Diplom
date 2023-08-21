from django.contrib import admin

from .models import Room, Review








@admin.register(Room)
class AdminRoom(admin.ModelAdmin):
    list_display_links = ('name_room',)
    list_display = ('name_room', 'content', 'price', 'room_photo')


@admin.register(Review)
class AdminReview(admin.ModelAdmin):
    list_display_links = ('author',)
    list_display = ('room', 'author', 'name_comment', 'created', 'content', 'rating_average')







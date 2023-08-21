from django.contrib import admin

from .models import Room, Review, DoubleRoom, DeluxeRoom, SuperiorRoom, PhotoDetailRoom


@admin.register(DoubleRoom)
class AdminPhotoDetailRoom(admin.ModelAdmin):
    list_display = ('price', 'add_photo', 'room')


@admin.register(DeluxeRoom)
class AdminPhotoDetailRoom(admin.ModelAdmin):
    list_display = ('price', 'add_photo', 'room')


@admin.register(SuperiorRoom)
class AdminPhotoDetailRoom(admin.ModelAdmin):
    list_display = ('price', 'add_photo', 'room')


@admin.register(Room)
class AdminRoom(admin.ModelAdmin):
    list_display_links = ('name_room',)
    list_display = ('name_room', 'content', 'price', 'room_photo')


@admin.register(PhotoDetailRoom)
class AdminRoom(admin.ModelAdmin):
    list_display = ('room', 'add_photo')



@admin.register(Review)
class AdminReview(admin.ModelAdmin):
    list_display_links = ('author',)
    list_display = ('room', 'author', 'name_comment', 'created', 'content', 'rating_average')

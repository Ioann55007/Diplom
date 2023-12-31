from django.contrib import admin

from .models import Room, Review, DoubleRoom, DeluxeRoom, SuperiorRoom, PhotoDetailRoom


@admin.register(DoubleRoom)
class AdminDoubleRoom(admin.ModelAdmin):
    list_display = ('price', 'add_photo', 'room', 'content')


@admin.register(DeluxeRoom)
class AdminDeluxeRoom(admin.ModelAdmin):
    list_display = ('price', 'add_photo', 'room', 'content')


@admin.register(SuperiorRoom)
class AdminSuperiorRoom(admin.ModelAdmin):
    list_display = ('price', 'add_photo', 'room', 'content')


@admin.register(Room)
class AdminRoom(admin.ModelAdmin):
    list_display_links = ('name_room',)
    list_display = ('name_room', 'content', 'price', 'room_photo')


@admin.register(PhotoDetailRoom)
class AdminPhotoDetailRoom(admin.ModelAdmin):
    list_display = ('room', 'add_photo')


@admin.register(Review)
class AdminReview(admin.ModelAdmin):
    list_display_links = ('author',)
    list_display = ('room', 'author', 'name_comment', 'created', 'content', 'rating_average')

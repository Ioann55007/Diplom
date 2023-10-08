from django.contrib import admin

from .models import Profile
from part_room.models import User


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display_links = ('username',)
    list_display = ('username', 'email', 'first_name', 'last_name', 'created', 'phone')
    prepopulated_fields = {'slug': ('username',)}



@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display_links = ('username',)
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone')

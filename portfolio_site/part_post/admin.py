from django.contrib import admin

from .models import NewPost, Comment


@admin.register(NewPost)
class AdminNewPost(admin.ModelAdmin):
    list_display_links = ('name_new_post', 'author')
    list_display = ('name_new_post', 'author', 'content', 'data_published')




@admin.register(Comment)
class AdminNewPost(admin.ModelAdmin):
    list_display_links = ('author', 'new_post')
    list_display = ('author', 'new_post', 'content', 'created')

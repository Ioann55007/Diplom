from django.contrib import admin

from .models import NewPost, Comment


@admin.register(NewPost)
class AdminNewPost(admin.ModelAdmin):
    list_display_links = ('name_new_post',)
    list_display = ('name_new_post', 'content', 'data_published', 'image_post')
    prepopulated_fields = {'slug': ('name_new_post',)}




@admin.register(Comment)
class AdminCommentPost(admin.ModelAdmin):
    list_display_links = ('new_post',)
    list_display = ('new_post', 'content', 'created')

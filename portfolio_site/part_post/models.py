from django.conf import settings
from django.db import models


from part_room.models import User


class NewPost(models.Model):
    name_new_post = models.CharField(max_length=300)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    data_published = models.DateField(auto_now_add=True)


class Comment(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment_author')
    new_post = models.ForeignKey(NewPost, on_delete=models.CASCADE, related_name='comment_new_post')
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
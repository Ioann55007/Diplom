from django.contrib.auth.models import User
from django.db import models


class NewPost(models.Model):
    name_new_post = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    data_published = models.DateField(auto_now_add=True)


class Comment(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    new_post = models.ForeignKey(NewPost, on_delete=models.CASCADE, related_name='comment_new_post')
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
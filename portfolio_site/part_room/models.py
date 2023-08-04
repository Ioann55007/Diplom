from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    name_room = models.CharField(max_length=300)
    content = models.TextField()
    price = models.IntegerField()
    room_photo = models.ImageField(upload_to='')


class Review(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_author')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='review_post')
    name_comment = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    rating_average = models.IntegerField(default=0)

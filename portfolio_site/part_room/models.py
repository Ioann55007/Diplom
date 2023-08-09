from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Room(models.Model):
    objects = models.Manager()
    name_room = models.CharField(max_length=300)
    content = models.TextField()
    price = models.IntegerField()
    room_photo = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return f"{self.name_room}"

    def get_absolute_url(self):
        return reverse('room-detail', kwargs={'id': self.name_room})


class Images(models.Model):
  image = models.ImageField(upload_to='')
  room = models.ForeignKey(Room, related_name="several_image", on_delete=models.CASCADE)



class Review(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_author')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='review_post')
    name_comment = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    rating_average = models.IntegerField(default=0)

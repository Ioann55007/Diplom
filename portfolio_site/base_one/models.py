from django.db import models

from the_profile.models import Profile
from part_room.models import Room


class ReviewHotel(models.Model):
    objects = models.Manager()
    name_author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='name_author')
    created = models.DateTimeField(auto_now_add=True)
    text_review = models.TextField()



class BookingHotel(models.Model):
    objects = models.Manager()
    user_booking = models.ForeignKey(Profile, on_delete=models.CASCADE)
    arrival_date = models.DateTimeField()
    date_of_departure = models.DateTimeField()
    # room_booking = models.CharField(max_length=100)
    room_booking = models.ForeignKey(Room, on_delete=models.CASCADE)
    adults = models.PositiveIntegerField()
    childs = models.PositiveIntegerField()
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return f"{self.room_booking}"

    def sum(self):
        return f"{(self.adults + self.childs) * self.room_booking.price}"




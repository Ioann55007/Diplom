from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

from django.contrib.auth.models import PermissionsMixin, UserManager

from the_profile.models import Profile

from base_one.models import BookingHotel
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    phone = models.CharField(max_length=100)
    date_joined = models.DateTimeField(u'date joined', default=timezone.now)
    objects = UserManager()
    avatar = models.ImageField(settings.AUTH_USER_MODEL, default='/No-Image-Available.jpg', blank=True)
    USERNAME_FIELD = 'username'
    is_verify_email = models.BooleanField(default=False, verbose_name="Подтверждение электронной почты")

    REQUIRED_FIELDS = ['email', 'password', 'avatar', 'phone']

    def __str__(self):
        return f"{self.first_name}"


class Room(models.Model):
    objects = models.Manager()
    name_room = models.CharField(max_length=300)
    content = models.TextField()
    price = models.IntegerField()
    room_photo = models.ImageField(upload_to='', blank=True)
    booking = models.ForeignKey(BookingHotel, on_delete=models.CASCADE, related_name='booking_room',
                                null=True, blank=True)

    def __str__(self):
        return f"{self.name_room}"

    def get_absolute_url(self):
        return reverse('room-detail', kwargs={'id': self.name_room})


class PhotoDetailRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='photo_room',
                             verbose_name='Номер в гостинице')
    add_photo = models.ImageField(upload_to="image_room/", blank=True, verbose_name='Фото')

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'Изображения'


class DoubleRoom(models.Model):
    objects = models.Manager()
    price = models.PositiveIntegerField()
    add_photo = models.ImageField(upload_to="image_room/", verbose_name='Фото')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_double',
                             verbose_name='Номер в гостинице')
    content = models.TextField()

    class Meta:
        verbose_name = 'изображение Double Room'
        verbose_name_plural = 'Фото Double Room'


class DeluxeRoom(models.Model):
    objects = models.Manager()
    price = models.PositiveIntegerField()
    add_photo = models.ImageField(upload_to="image_room/", verbose_name='Фото')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='deluxe_room',
                             verbose_name='Номер в гостинице')
    content = models.TextField()

    class Meta:
        verbose_name = 'изображение Deluxe Room'
        verbose_name_plural = 'Фото Deluxe Room'


class SuperiorRoom(models.Model):
    price = models.PositiveIntegerField()
    add_photo = models.ImageField(upload_to="image_room/", verbose_name='Фото')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='superior_room',
                             verbose_name='Номер в гостинице')
    content = models.TextField()

    class Meta:
        verbose_name = 'изображение Superior Room'
        verbose_name_plural = 'Фото Superior Room'


class Review(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='review_author')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='review_post')
    name_comment = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    rating_average = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.author}, {self.room}"







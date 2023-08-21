from django.conf import settings
from django.db import models



class Profile(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(default='no-image-available.jpg', blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True, verbose_name='Email')
    username = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=100, verbose_name='Phone')


def __str__(self):
    return f"{self.username}"

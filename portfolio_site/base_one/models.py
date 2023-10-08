from django.db import models

from the_profile.models import Profile



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
    adults = models.PositiveIntegerField()
    childs = models.PositiveIntegerField()
    quantity = models.IntegerField(default=1)
    price = models.PositiveIntegerField()


class Restaurant(models.Model):
    title = models.CharField(max_length=210)
    photo = models.ImageField(upload_to='restaraunts/')
    average_bill = models.PositiveIntegerField(default=0)
    description = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return f"{self.title}"


class PhotoDishRestaurant(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='photo_dish',
                                   verbose_name='Photo dish')
    add_photo = models.ImageField(upload_to="photo_restaurant/", blank=True, verbose_name='Фото')

    def __str__(self):
        return f"{self.restaurant}"

    class Meta:
        verbose_name = 'dish'
        verbose_name_plural = 'Dishes'



class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}"




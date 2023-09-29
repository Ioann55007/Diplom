from django.forms import ModelForm
from .models import ReviewHotel


class ReviewHotelForm(ModelForm):

    class Meta:
        model = ReviewHotel
        fields = ('name_author', 'text_review')





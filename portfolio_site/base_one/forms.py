import datetime

from django import forms
from django.forms import ModelForm, DateInput
from .models import ReviewHotel, BookingHotel, ContactModel
from part_room.models import Room
from the_profile.models import Profile


class ReviewHotelForm(ModelForm):
    class Meta:
        model = ReviewHotel
        fields = ('name_author', 'text_review')


class BookingForm(forms.ModelForm):
    arrival_date = forms.DateTimeField(required=False, widget=DateInput(attrs={'type': 'datetime-local'}),
                                       initial=datetime.date.today(), localize=True)
    date_of_departure = forms.DateTimeField(required=False, widget=DateInput(attrs={'type': 'datetime-local'}),
                                            initial=datetime.date.today(), localize=True)
    user_booking = forms.ModelChoiceField(widget=forms.HiddenInput,  queryset=Profile.objects.all(), required=False, label='Profile')
    room_booking = forms.ModelChoiceField(widget=forms.HiddenInput, queryset=Room.objects.all(), required=False, label='Room')
    adults = forms.IntegerField()
    childs = forms.IntegerField()
    quantity = forms.IntegerField()


    class Meta:
        model = BookingHotel
        fields = ('arrival_date', 'date_of_departure', 'user_booking', 'room_booking', 'adults', 'childs')



class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

    class Meta:
        model = ContactModel
        fields = ("name", "last_name", "email", "phone", "message")



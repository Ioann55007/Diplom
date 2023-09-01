from django import forms
from django.forms import ModelForm
from django import forms
from .models import Review


class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

    class Meta:
        model = Review
        fields = ('name_comment', 'content', 'author')





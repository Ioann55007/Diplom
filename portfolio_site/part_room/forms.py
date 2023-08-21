# from django import forms
# from django.forms import ModelForm
#
# from .models import Review
#
#
# class ReviewForm(ModelForm):
#     class Meta:
#         model = Review
#         fields = ['author', 'name_comment', 'content', 'rating_average', 'room']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         for name, field in self.fields.items():
#             field.widget.attrs.update({'class': 'input'})
#
#
#

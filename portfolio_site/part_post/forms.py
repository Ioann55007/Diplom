from django import forms
from django.forms import HiddenInput

from .models import Comment


class CommentForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'input'})

    # def __init__(self, *args, **kwargs):
    #     super(TagStatusForm, self).__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget = forms.HiddenInput()

    class Meta:
        model = Comment
        fields = ('content',)

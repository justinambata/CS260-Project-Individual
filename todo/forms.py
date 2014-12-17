from django import forms
from django.core.exceptions import ValidationError

from todo.models import Item

import datetime

class ItemForm(forms.ModelForm):
    description = forms.CharField(
        max_length=250,
        help_text="Item description:",
        required=True)

    created_date = forms.DateTimeField(widget=forms.HiddenInput(), initial=datetime.datetime.now)

    class Meta:
        model = Item
        exclude = ('owner',)
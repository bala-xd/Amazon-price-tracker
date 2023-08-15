from django import forms
from django.forms.models import ModelForm
from .models import Link

class AddLinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ('url',)
from django import forms
from . import models


class CreateProfile(forms.ModelForm):
    class Meta():
        model = models.Profile
        fields = []


class Follow_form(forms.ModelForm):
    class Meta():
        model = models.Follow
        fields = []

from django import forms
from django.contrib.auth.models import User
from .models import ProfilesModel

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfilesModel
        fields = ('bio', 'location', 'birth_date')

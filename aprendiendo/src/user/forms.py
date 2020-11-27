from django import forms

from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'number',
            'password'

        ]


class RawUserForm(forms.Form):
    name = forms.CharField(required=False)
    number = forms.CharField()
    password = forms.CharField()

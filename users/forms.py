from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=True)
    # last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = (
            # 'first_name',
            # 'last_name',
            'username',
            'email',
            'phone_number',
            'password1',
            'password2',
            'is_artist',
            'is_curator',
            'is_viewer'
        )

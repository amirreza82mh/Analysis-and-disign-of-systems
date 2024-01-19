from django import forms
from django.core.validators import RegexValidator, MaxLengthValidator, MinLengthValidator
from django.contrib.auth.forms import UserCreationForm
from .models import User


password_validator = RegexValidator(
    regex=r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$",
    message='Minimum eight characters, at least one letter, one number and one special character:',
    code='invalid_password'
)


username_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9_]+$',
    message='Enter a valid username. Only alphanumeric characters and underscores are allowed.',
    code='invalid_username'
)


email_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9_.+-]+@gmail\.com$',
    message='Enter a valid email address.',
    code='invalid_email'
)


phone_number_validator = RegexValidator(
    regex=r'^09[0-9]{9}$',
    message='Enter a valid phone number',
    code='invalid phone number'
)


class SignUpForm(forms.Form):
    username = forms.CharField(validators=[username_validator])
    email = forms.EmailField(validators=[email_validator])
    phone_number = forms.CharField(validators=[phone_number_validator])

    password1 = forms.CharField(
        widget=forms.PasswordInput(),
        validators=[password_validator]
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        validators=[password_validator]
    )

    is_curator = forms.BooleanField(required=False)
    is_artist = forms.BooleanField(required=False)
    is_viewer = forms.BooleanField(required=False)


class LoginForm(forms.Form):
    username = username = forms.CharField(validators=[username_validator])

    password = forms.CharField(
        widget=forms.PasswordInput(),
        validators=[password_validator]
    )


class UpdateForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField(validators=[email_validator])
    phone_number = forms.CharField(validators=[phone_number_validator])
    username = forms.CharField(validators=[username_validator])
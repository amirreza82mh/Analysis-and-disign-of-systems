from django import forms
from django.core.validators import RegexValidator


email_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9_.+-]+@gmail\.com$',
    message='Enter a valid email address.',
    code='invalid_email'
)


class ContactForm(forms.Form):
    first_last_name = forms.CharField(max_length=100)
    email = forms.EmailField(validators=[email_validator])
    subject = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea())


class ReserveForm(forms.Form):
    date = forms.DateField()
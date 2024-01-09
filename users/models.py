from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):

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

    username = models.CharField(max_length=50, unique=True, null=False, validators=[username_validator])
    email = models.EmailField(null=False, validators=[email_validator], unique=True)
    phone_number = models.CharField(max_length=11, null=False, unique=True, validators=[phone_number_validator]) 

    is_artist = models.BooleanField('is artist', default=False)
    is_curator = models.BooleanField('is curator', default=False)
    is_viewer = models.BooleanField('is viewer', default=False)


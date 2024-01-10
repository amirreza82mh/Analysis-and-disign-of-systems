from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, null=False)
    email = models.EmailField(null=False, unique=True)
    phone_number = models.CharField(max_length=11, null=False, unique=True) 
    is_artist = models.BooleanField('is artist', default=False)
    is_curator = models.BooleanField('is curator', default=False)
    is_viewer = models.BooleanField('is viewer', default=False)


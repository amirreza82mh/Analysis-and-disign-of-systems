from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_artist = models.BooleanField('is artist', default=False)
    is_curator = models.BooleanField('is curator', default=False)
    is_viewer = models.BooleanField('is viewer', default=False)


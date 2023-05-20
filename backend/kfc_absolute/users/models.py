from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    full_name = models.CharField(max_length=255, default='')
    repeat_password = models.CharField(max_length=50, default='')

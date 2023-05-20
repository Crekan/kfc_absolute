from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    full_name = models.CharField(max_length=255, null=True)
    repeat_password = models.CharField(max_length=50, null=True)

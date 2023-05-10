from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    middle_name = models.CharField(max_length=50)
    repeat_password = models.CharField(max_length=50, null=True)


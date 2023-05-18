from django.db import models
from django.utils import timezone

from users.models import User


class Temporary(models.Model):
    DAY_CHOICES = (
        ('Понедельник', 'Понедельник'),
        ('Вторник', 'Вторник'),
        ('Среда', 'Среда'),
        ('Четверг', 'Четверг'),
        ('Пятница', 'Пятница'),
        ('Суббота', 'Суббота'),
        ('Восересенье', 'Восересенье'),
    )
    SHIFT_CHOICES = (
        ('FT', 'FT'),
        ('Первая смена', 'Первая смена'),
        ('Вторая смена', 'Вторая смена'),
        ('Выходной', 'Выходной'),
        ('Другое', 'Другое'),
    )

    day = models.CharField(max_length=20, choices=DAY_CHOICES)
    shift_type = models.CharField(max_length=30, choices=SHIFT_CHOICES)
    custom_time = models.CharField(max_length=255, null=True, blank=True)
    date_add = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    night = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.day} - {self.shift_type}'

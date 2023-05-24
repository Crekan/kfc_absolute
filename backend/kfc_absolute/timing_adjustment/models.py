from django.db import models

from users.models import User


class ShiftManager(models.Model):
    full_name = models.CharField(max_length=150)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'


class AdjustmentWorkingHours(models.Model):
    LUNCH_CHOICES = (
        ('Перерыв 15 минут', 'Перерыв 15 минут'),
        ('Перерыв 30 минут', 'Перерыв 30 минут'),
        ('Без перерыва', 'Без перерыва'),
        ('Другое', 'Другое'),
    )

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    launch = models.CharField(max_length=150, choices=LUNCH_CHOICES)
    manager = models.ForeignKey(ShiftManager, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def formatted_start_time(self):
        return self.start_time.strftime('%H:%M')

    def formatted_end_time(self):
        return self.end_time.strftime('%H:%M')

    def __str__(self):
        return f'{self.launch} - {self.manager}'

    class Meta:
        verbose_name = 'Корректировка рабочего времени'
        verbose_name_plural = 'Корректировка рабочего времени'

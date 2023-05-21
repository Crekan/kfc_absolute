from django.db import models

from users.models import User


class Vakantie(models.Model):
    TYPE_VERLOF_CHOICES = (
        ('Трудовой(оплачиваемый)', 'Трудовой(оплачиваемый)'),
        ('Социальный(за свой счет)', 'Социальный(за свой счет)'),
    )

    vakantie = models.CharField(max_length=150, choices=TYPE_VERLOF_CHOICES)
    start_vacation = models.DateField()
    end_vacation = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.vakantie} с {self.start_vacation}'

    class Meta:
        verbose_name = 'Заявка на отпуск'
        verbose_name_plural = 'Заявка на отпуски'

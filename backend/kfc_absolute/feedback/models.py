from django.db import models


class Feedback(models.Model):
    TYPE_TREATMENT_CHOICES = (
        ('жалоба', 'жалоба'),
        ('Предложение/идея', 'Предложение/идея'),
        ('Похвала', 'Похвала'),
        ('Другое', 'Другое'),
    )
    FOR_WHOM_CHOICES = (
        ('Весь управляющий состав (зам. директора и директор)', 'Весь управляющий состав (зам. директора и директор)'),
        ('Весь менеджерский состав', 'Весь менеджерский состав'),
        ('Весь состав тренеров', 'Весь состав тренеров'),
        ('Весь состав ЧК', 'Весь состав ЧК'),
        ('Всю команду', 'Всю команду'),
        ('Другое', 'Другое'),
    )

    address = models.CharField(max_length=150, choices=TYPE_TREATMENT_CHOICES)
    team = models.CharField(max_length=255, choices=FOR_WHOM_CHOICES)
    situation = models.TextField()
    other = models.TextField(blank=True)

    def __str__(self):
        return f'{self.address} - {self.team}'

    class Meta:
        verbose_name = 'Обрантая связь'
        verbose_name_plural = 'Обрантая связь'

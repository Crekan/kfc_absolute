# Generated by Django 4.2.1 on 2023-05-21 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vakantie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vakantie',
            name='end_vacation',
            field=models.DateTimeField(blank=True),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-18 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='middle_name',
        ),
        migrations.AddField(
            model_name='user',
            name='fill_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

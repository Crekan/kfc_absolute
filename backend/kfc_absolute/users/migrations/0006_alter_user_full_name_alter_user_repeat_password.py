# Generated by Django 4.2.1 on 2023-05-20 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_full_name_alter_user_repeat_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='repeat_password',
            field=models.CharField(default='', max_length=50),
        ),
    ]

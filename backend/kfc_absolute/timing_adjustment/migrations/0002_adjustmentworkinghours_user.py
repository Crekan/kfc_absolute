# Generated by Django 4.2.1 on 2023-05-24 08:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timing_adjustment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adjustmentworkinghours',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
# Generated by Django 5.0.6 on 2024-10-14 22:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0027_alter_list_user_alter_twilioinfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.user'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-10-10 11:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0024_contact_user_list_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.user'),
        ),
        migrations.AlterField(
            model_name='list',
            name='user',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.user'),
        ),
    ]

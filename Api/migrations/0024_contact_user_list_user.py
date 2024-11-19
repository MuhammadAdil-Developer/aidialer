# Generated by Django 5.0.6 on 2024-10-10 11:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0023_list_created_at_list_updated_at_alter_contact_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Api.user'),
        ),
        migrations.AddField(
            model_name='list',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Api.user'),
        ),
    ]

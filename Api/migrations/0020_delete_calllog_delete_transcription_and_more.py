# Generated by Django 5.0.6 on 2024-09-08 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0019_user_usertoken'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CallLog',
        ),
        migrations.DeleteModel(
            name='Transcription',
        ),
        migrations.AddField(
            model_name='agentresponse',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Api.user'),
        ),
        migrations.AddField(
            model_name='promptrecord',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Api.user'),
        ),
        migrations.AddField(
            model_name='twilioinfo',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Api.user'),
        ),
        migrations.AlterField(
            model_name='usertoken',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Api.user'),
        ),
    ]
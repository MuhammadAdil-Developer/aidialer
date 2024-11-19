# Generated by Django 5.0.6 on 2024-08-27 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0006_agentresponse_analysis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agentresponse',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='agentresponse',
            name='call_duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='agentresponse',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='agentresponse',
            name='messages',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='agentresponse',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
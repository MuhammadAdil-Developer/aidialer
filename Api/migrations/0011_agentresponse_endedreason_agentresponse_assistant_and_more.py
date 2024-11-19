# Generated by Django 5.0.6 on 2024-08-30 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0010_agentresponse_call_type_agentresponse_from_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentresponse',
            name='EndedReason',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='agentresponse',
            name='assistant',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='agentresponse',
            name='cost',
            field=models.FloatField(default='0.0'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-09-08 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0016_agentresponse_created_at_agentresponse_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agentresponse',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='agentresponse',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='agentresponse',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='promptrecord',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

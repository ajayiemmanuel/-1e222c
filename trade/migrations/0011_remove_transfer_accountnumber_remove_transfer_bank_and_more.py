# Generated by Django 5.0.7 on 2024-07-13 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0010_banktransfer_rate_bitcoin_rate_transfer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='accountnumber',
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='bank',
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='swift',
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='wallet',
        ),
    ]

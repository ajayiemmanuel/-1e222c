# Generated by Django 5.0.7 on 2024-07-12 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_deposit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposit',
            name='total_invest',
        ),
    ]

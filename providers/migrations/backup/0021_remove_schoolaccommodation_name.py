# Generated by Django 5.0.6 on 2024-07-19 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0020_remove_schoolaccommodation_name_accommodation_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolaccommodation',
            name='name',
        ),
    ]

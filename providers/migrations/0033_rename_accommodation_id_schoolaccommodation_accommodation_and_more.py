# Generated by Django 5.0.6 on 2024-07-30 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0032_school_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schoolaccommodation',
            old_name='accommodation_id',
            new_name='accommodation',
        ),
        migrations.RenameField(
            model_name='schoolaccommodation',
            old_name='school_id',
            new_name='school',
        ),
    ]

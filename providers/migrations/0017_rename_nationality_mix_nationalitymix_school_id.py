# Generated by Django 5.0.6 on 2024-07-08 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0016_classroomequipment_alter_accommodation_img_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nationalitymix',
            old_name='nationality_mix',
            new_name='school_id',
        ),
    ]

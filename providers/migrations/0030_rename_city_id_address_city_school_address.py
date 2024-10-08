# Generated by Django 5.0.6 on 2024-07-29 21:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0029_remove_school_courses_course_school'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='city_id',
            new_name='city',
        ),
        migrations.AddField(
            model_name='school',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='providers.address'),
        ),
    ]

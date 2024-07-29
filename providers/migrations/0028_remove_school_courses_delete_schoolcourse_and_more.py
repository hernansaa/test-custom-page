# Generated by Django 5.0.6 on 2024-07-29 20:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0027_course_schoolcourse_school_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='courses',
        ),
        migrations.DeleteModel(
            name='SchoolCourse',
        ),
        migrations.AddField(
            model_name='school',
            name='courses',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='providers.course'),
        ),
    ]

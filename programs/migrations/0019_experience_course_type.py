# Generated by Django 5.0.6 on 2024-08-15 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0018_alter_experience_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='course_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='programs.coursetype'),
        ),
    ]

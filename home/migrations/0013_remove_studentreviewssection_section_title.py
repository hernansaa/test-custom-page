# Generated by Django 5.0.6 on 2024-08-19 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_rename_studentreview_studentreviewssection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentreviewssection',
            name='section_title',
        ),
    ]

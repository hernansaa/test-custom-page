# Generated by Django 5.0.6 on 2024-08-31 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_alter_studentprofile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='status',
            field=models.CharField(blank=True, choices=[('enrolled', 'Enrolled'), ('not enrolled', 'Not enrolled'), ('studying', 'Studying')], default='not enrolled', max_length=255, null=True, verbose_name='status'),
        ),
    ]

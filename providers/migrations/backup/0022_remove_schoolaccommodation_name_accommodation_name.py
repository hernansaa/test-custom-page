# Generated by Django 5.0.6 on 2024-07-19 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0021_school_school_accommodation'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodation',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-05 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0005_alter_activity_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='activities',
            field=models.ManyToManyField(through='providers.SchoolActivity', to='providers.activity'),
        ),
    ]

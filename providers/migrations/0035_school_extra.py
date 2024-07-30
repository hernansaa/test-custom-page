# Generated by Django 5.0.6 on 2024-07-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0034_rename_airport_id_schoolairporttransfer_airport_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='extra',
            field=models.ManyToManyField(blank=True, null=True, through='providers.SchoolExtra', to='providers.extra'),
        ),
    ]

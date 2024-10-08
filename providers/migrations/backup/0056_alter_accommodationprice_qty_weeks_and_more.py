# Generated by Django 5.0.6 on 2024-08-06 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0055_alter_schoolairporttransfer_trip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodationprice',
            name='qty_weeks',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='courseprice',
            unique_together={('course', 'weeks')},
        ),
    ]

# Generated by Django 5.0.6 on 2024-08-03 09:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0048_accommodationprice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolaccommodation',
            name='price_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='providers.accommodationpricelist'),
        ),
    ]

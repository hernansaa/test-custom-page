# Generated by Django 5.0.6 on 2024-08-03 15:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiries', '0023_rename_qty_weeks_enquiry_course_qty_weeks'),
        ('providers', '0052_alter_accommodationprice_accommodation_price_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='accommodation_qty_weeks',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='providers.accommodationprice'),
        ),
    ]

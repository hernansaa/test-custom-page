# Generated by Django 5.0.6 on 2024-08-27 13:03

import django.db.models.deletion
import smart_selects.db_fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0065_rename_price_courseprice_week_price_promotional_and_more'),
        ('quotations', '0016_alter_quotation_accommodation_price_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='accommodation_price_list',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='schoo_accommodation_id', chained_model_field='school_accommodation_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='providers.accommodationpricelist'),
        ),
    ]

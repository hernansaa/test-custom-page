# Generated by Django 5.0.6 on 2024-08-28 21:22

import django.db.models.deletion
import smart_selects.db_fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0008_alter_invoice_school'),
        ('providers', '0065_rename_price_courseprice_week_price_promotional_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='accommodation',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='school', chained_model_field='school', null=True, on_delete=django.db.models.deletion.CASCADE, to='providers.schoolaccommodation'),
        ),
    ]

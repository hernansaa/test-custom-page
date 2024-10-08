# Generated by Django 5.0.6 on 2024-08-15 10:12

import django.db.models.deletion
import smart_selects.db_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0015_rename_course_type_id_coursetype_id'),
        ('providers', '0065_rename_price_courseprice_week_price_promotional_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='course_description',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='course_end_date',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='course_name',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='course_start_date',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='course_type',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='course_weeks_duration',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='school_name',
        ),
        migrations.AddField(
            model_name='experience',
            name='course',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='school', chained_model_field='school', default='1', on_delete=django.db.models.deletion.CASCADE, to='providers.course'),
        ),
        migrations.AddField(
            model_name='experience',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='providers.school'),
        ),
    ]

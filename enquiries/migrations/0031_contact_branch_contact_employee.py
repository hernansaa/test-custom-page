# Generated by Django 5.0.6 on 2024-08-18 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0007_agencybranch_apartment_number_and_more'),
        ('enquiries', '0030_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='branches.agencybranch'),
        ),
        migrations.AddField(
            model_name='contact',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='branches.employeeprofile'),
        ),
    ]

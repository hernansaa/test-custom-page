# Generated by Django 5.0.6 on 2024-07-06 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0013_alter_schoolextra_extra_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvgAges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_age', models.IntegerField(blank=True, null=True)),
                ('to_age', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolAvgAges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('avg_ages_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.avgages')),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.school')),
            ],
        ),
    ]

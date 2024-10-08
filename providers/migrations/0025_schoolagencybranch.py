# Generated by Django 5.0.6 on 2024-07-19 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0004_alter_agencybranch_telephone'),
        ('providers', '0024_schoolagencybranch'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolAgencyBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branches.agencybranch')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.school')),
            ],
        ),
    ]

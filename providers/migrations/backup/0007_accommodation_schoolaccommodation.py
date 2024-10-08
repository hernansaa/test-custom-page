# Generated by Django 5.0.6 on 2024-07-05 23:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0006_school_activities'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='schools/Accommodation')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolAccommodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('accommodation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.accommodation')),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.school')),
            ],
        ),
    ]

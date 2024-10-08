# Generated by Django 5.0.6 on 2024-07-05 22:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0002_alter_facility_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acreditation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='schools/Acreditations')),
            ],
        ),
        migrations.RenameField(
            model_name='school',
            old_name='Facilities',
            new_name='facilities',
        ),
        migrations.CreateModel(
            name='SchoolAcreditation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acreditation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.acreditation')),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.school')),
            ],
        ),
        migrations.AddField(
            model_name='school',
            name='acreditations',
            field=models.ManyToManyField(through='providers.SchoolAcreditation', to='providers.acreditation'),
        ),
    ]

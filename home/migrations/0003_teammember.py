# Generated by Django 5.0.6 on 2024-08-16 16:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_aboutus_content_sub_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('photo', models.ImageField(upload_to='team_photos/')),
                ('about_us_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='home.aboutus')),
            ],
        ),
    ]

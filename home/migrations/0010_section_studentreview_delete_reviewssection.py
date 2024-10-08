# Generated by Django 5.0.6 on 2024-08-19 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_homepage_reviewssection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='StudentReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('age', models.IntegerField()),
                ('profile_img', models.ImageField(blank=True, null=True, upload_to='home/home/reviews')),
                ('review', models.TextField()),
                ('review_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.section')),
            ],
        ),
        migrations.DeleteModel(
            name='ReviewsSection',
        ),
    ]

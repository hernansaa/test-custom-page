# Generated by Django 5.0.6 on 2024-06-25 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0012_rename_experience_name_experience_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='img',
            field=models.ImageField(upload_to='programs/'),
        ),
    ]

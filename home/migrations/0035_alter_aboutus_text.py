# Generated by Django 5.0.6 on 2024-08-29 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_alter_aboutus_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]

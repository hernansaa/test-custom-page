# Generated by Django 5.0.6 on 2024-08-06 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='currency',
            name='symbol',
            field=models.CharField(max_length=10),
        ),
    ]

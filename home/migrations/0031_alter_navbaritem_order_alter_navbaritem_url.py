# Generated by Django 5.0.6 on 2024-08-20 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_navbaritem_home_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbaritem',
            name='order',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='navbaritem',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]

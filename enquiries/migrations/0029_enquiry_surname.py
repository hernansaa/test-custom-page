# Generated by Django 5.0.6 on 2024-08-14 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiries', '0028_enquiry_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='surname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

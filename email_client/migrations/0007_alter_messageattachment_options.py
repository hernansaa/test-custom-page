# Generated by Django 5.0.6 on 2024-06-28 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_client', '0006_alter_messageattachment_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messageattachment',
            options={'verbose_name': 'Attachment', 'verbose_name_plural': 'Attachments'},
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-27 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_mailbox', '0009_alter_message_eml'),
        ('email_client', '0005_rename_message_proxymessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('django_mailbox.message',),
        ),
        migrations.DeleteModel(
            name='ProxyMessage',
        ),
    ]

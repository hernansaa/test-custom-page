# Generated by Django 5.0.6 on 2024-06-27 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_mailbox', '0009_alter_message_eml'),
        ('email_client', '0004_messageattachment_rename_custommessage_message_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='message_ptr',
        ),
        migrations.RemoveField(
            model_name='messageattachment',
            name='messageattachment_ptr',
        ),
        migrations.DeleteModel(
            name='CustomMailbox',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='MessageAttachment',
        ),
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
        migrations.CreateModel(
            name='MessageAttachment',
            fields=[
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('django_mailbox.messageattachment',),
        ),
    ]

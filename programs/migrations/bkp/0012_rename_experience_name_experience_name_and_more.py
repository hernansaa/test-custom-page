# Generated by Django 5.0.6 on 2024-06-25 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0011_alter_experience_max_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='experience_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='experience_id',
        ),
        migrations.AddField(
            model_name='experience',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]

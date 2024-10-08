# Generated by Django 5.0.6 on 2024-08-31 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0003_alter_transaction_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='type',
            field=models.CharField(blank=True, choices=[('in', 'In'), ('out', 'Out')], max_length=255, null=True, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='payment_method',
            field=models.CharField(choices=[('CREDIT_CARD', 'Credit Card'), ('BANK_TRANSFER', 'Bank Transfer'), ('PAYPAL', 'PayPal'), ('CASH', 'Cash'), ('OTHER', 'Other')], max_length=25),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed'), ('FAILED', 'Failed'), ('CANCELLED', 'Cancelled'), ('REFUNDED', 'Refunded')], default='PENDING', max_length=25),
        ),
    ]

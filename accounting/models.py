from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from currencies.models import Currency
from invoices.models import Invoice



class TransactionType(models.TextChoices):
        IN = "in", _("In")
        OUT = "out", _("Out")


class Transaction(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('CREDIT_CARD', 'Credit Card'),
        ('BANK_TRANSFER', 'Bank Transfer'),
        ('PAYPAL', 'PayPal'),
        ('CASH', 'Cash'),
        ('OTHER', 'Other'),
    ]

    TRANSACTION_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
        ('CANCELLED', 'Cancelled'),
        ('REFUNDED', 'Refunded'),
    ]

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='transactions')  # Foreign key to Course model
    type = models.CharField(_("status"), choices=TransactionType.choices, null=True, blank=True, max_length=255,)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Transaction amount
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)  # Currency code, e.g., USD, EUR
    payment_method = models.CharField(max_length=25, choices=PAYMENT_METHOD_CHOICES)  # Payment method used
    status = models.CharField(max_length=25, choices=TRANSACTION_STATUS_CHOICES, default='PENDING')  # Transaction status
    transaction_date = models.DateTimeField(default=timezone.now)  # Date and time of the transaction
    reference = models.CharField(max_length=200,blank=True, null=True)  
    description = models.TextField(blank=True, null=True)
    transaction_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)  # Fee associated with the transaction
    receipt = models.FileField(upload_to='receipts/', blank=True, null=True)  # URL to the receipt, if applicable
    related_transactions = models.ManyToManyField('self', blank=True)  # Link to related transactions, such as refunds

    def __str__(self):
        return f'Transaction {self.id} - {self.amount} {self.currency}'

    class Meta:
        ordering = ['-transaction_date']  # Order transactions by most recent

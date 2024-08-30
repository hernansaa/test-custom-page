from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from accounting.models import Transaction
from .models import Invoice
from quotations.models import Quotation


@receiver(post_save, sender=Quotation)
def create_invoice(sender, instance, created, **kwargs):
    if instance.status == 'approved':
        # Check if the invoice already exists for this quotation
        if not hasattr(instance, 'invoice'):
            # Generate a unique invoice number (last invoice id)
            if Invoice.objects.order_by('-id').first():
                invoice_number = int(Invoice.objects.order_by('-id').first().id) + 1 # Get the last invoice by ID
            else:
                invoice_number = 1

            Invoice.objects.create(
                quotation=instance,
                student = instance.student,
                invoice_number=invoice_number,
                total_amount=instance.total,
                enrollment_fee = instance.enrollment_fee,
                school = instance.school,
                course = instance.course,
                course_qty_weeks = instance.course_qty_weeks,
                course_date_start = instance.course_date_start,
                school_total = instance.school_total,
                accommodation = instance.accommodation,
                accommodation_qty_weeks = instance.accommodation_qty_weeks,
                accommodation_date_start=instance.accommodation_date_start,
                accommodation_total = instance.accommodation_total,
                airport_transfer = instance.airport_transfer,
                airport_transfer_total = instance.airport_transfer_total,
            )
        else:
            # Update the existing invoice using the update method
            Invoice.objects.filter(id=instance.invoice.id).update(
                student = instance.student,
                total_amount=instance.total,
                enrollment_fee=instance.enrollment_fee,
                school=instance.school,
                course=instance.course,
                course_qty_weeks=instance.course_qty_weeks,
                course_date_start=instance.course_date_start,
                school_total=instance.school_total,
                accommodation=instance.accommodation,
                accommodation_qty_weeks=instance.accommodation_qty_weeks,
                accommodation_date_start=instance.accommodation_date_start,
                accommodation_total=instance.accommodation_total,
                airport_transfer=instance.airport_transfer,
                airport_transfer_total=instance.airport_transfer_total,
            )


@receiver(post_save, sender=Transaction)
def update_invoice_paid_status_on_save(sender, instance, **kwargs):
    update_invoice_paid_status(instance.invoice)
    update_enrollment_fee_paid_status(instance.invoice)


@receiver(post_delete, sender=Transaction)
def update_invoice_paid_status_on_delete(sender, instance, **kwargs):
    update_invoice_paid_status(instance.invoice)
    update_enrollment_fee_paid_status(instance.invoice)


def update_invoice_paid_status(invoice):
    """
    Update the 'paid' status of the invoice based on the outstanding balance.
    """
    if invoice.outstanding_balance() <= 0:
        invoice.paid = True
    else:
        invoice.paid = False
    invoice.save()


def update_enrollment_fee_paid_status(invoice):
    """
    Update the 'enrollment_fee_paid' status of the invoice if the total paid
    is more than the enrollment fee.
    """
    if invoice.enrollment_fee:  # Check if there is an enrollment fee
        if invoice.total_paid() >= invoice.enrollment_fee:
            invoice.enrollment_fee_paid = True
        else:
            invoice.enrollment_fee_paid = False
        invoice.save()

from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.utils import timezone

from locations.models import City
from students.models import StudentProfile
from quotations.models import Quotation
from providers.models import (
    School, 
    Course, 
    CoursePrice, 
    SchoolAccommodation, 
    AccommodationPrice, 
    SchoolAirportTransfer
    )


class Invoice(models.Model):
    quotation = models.OneToOneField(Quotation, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, null=True, blank=True)
    invoice_number = models.CharField(max_length=20, unique=True)
    date_issued = models.DateField(auto_now_add=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    school = ChainedForeignKey(
        School,
        chained_field="city",
        chained_model_field="address__city",
        show_all=False,
        auto_choose=False,
        sort=True,
        null=True,
        blank=True,
        )
    course = ChainedForeignKey(
        Course, 
        chained_field="school",
        chained_model_field="school",
        show_all=False,
        auto_choose=False,
        sort=True,
        null=True,
        blank=True,
        )
    course_qty_weeks = ChainedForeignKey(
        CoursePrice, 
        chained_field="course_price_list",
        chained_model_field="course_price_list",
        show_all=False,
        auto_choose=False,
        sort=True,
        null=True,
        blank=True,
        )
    course_date_start = models.DateField(null=True, blank=True)
    school_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    accommodation = ChainedForeignKey(
        SchoolAccommodation, 
        chained_field="school",
        chained_model_field="school",
        show_all=False,
        auto_choose=False,
        sort=True,
        null=True,
        blank=True,
        )
    accommodation_qty_weeks = ChainedForeignKey(
        AccommodationPrice, 
        chained_field="accommodation_price_list",
        chained_model_field="accommodation_price_list",
        show_all=False,
        auto_choose=False,
        sort=True,
        null=True,
        blank=True,
        )
    accommodation_date_start = models.DateField(null=True, blank=True)
    accommodation_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    airport_transfer = ChainedForeignKey(
        SchoolAirportTransfer, 
        chained_field="school",
        chained_model_field="school",
        show_all=False,
        auto_choose=False,
        sort=True,
        null=True,
        blank=True,
        )
    airport_transfer_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    enrollment_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    enrollment_fee_paid = models.BooleanField(default=False) 
    paid = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice #{self.invoice_number} for {self.quotation.student}"
  
    def total_paid(self):
        return sum(payment.amount for payment in self.payments.all())

    def outstanding_balance(self):
        return self.total_amount - self.total_paid()
    

class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, choices=[
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('cash', 'Cash'),
        # Add other payment methods as needed
    ])
    reference_number = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"Payment of {self.amount} for Invoice #{self.invoice.invoice_number}"
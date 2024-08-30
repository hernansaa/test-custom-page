from django.db import models
from smart_selects.db_fields import ChainedForeignKey

from locations.models import City
from branches.models import AgencyBranch, EmployeeProfile
from students.models import StudentProfile
from invoices.models import Invoice
from providers.models import (
    School,
    Course, 
    CoursePrice, 
    SchoolAccommodation, 
    AccommodationPrice, 
    SchoolAirportTransfer,
    )


class Enrollment(models.Model):
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, null=True, blank=True)
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
    # school_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
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
    # accommodation_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
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
    # airport_transfer_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # enrollment_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # enrollment_fee_paid = models.BooleanField(default=False) 
    # paid = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"

from django.db import models
from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from smart_selects.db_fields import ChainedForeignKey

from locations.models import City
from enquiries.models import Enquiry
from students.models import StudentProfile
from branches.models import (
    AgencyBranch, 
    EmployeeProfile,
    )
from providers.models import (
    School, 
    Course,
    CoursePrice, 
    CoursePriceList, 
    SchoolAccommodation, 
    AccommodationPrice, 
    AccommodationPriceList, 
    SchoolAirportTransfer
    )


class QuotationStatus(TextChoices):
    APPROVED = "approved", _("Approved")
    PENDING = "pending", _("Pending")
    REJECTED = "rejected", _("Rejected")


class Quotation(models.Model):
    """
    Quotation model representing a student's quote for a course, which can
    create the invoice if the status is set to 'approved'.
    """

    QUOTATION_STATUS = (
        ('sent', 'sent'),
        ('approved', 'approved'),
        ('rejected', 'rejected'),
        ('expired', 'expired'),
    )

    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, null=True, blank=True)
    enquiry = ChainedForeignKey(
        Enquiry, 
        chained_field="student",
        chained_model_field="student",
        show_all=False,
        auto_choose=False,
        sort=True,
        null=True,
        blank=True,
        )
    # program = models.ForeignKey('providers.School', on_delete=models.CASCADE)
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
    course_price_list = ChainedForeignKey(
        CoursePriceList, 
        chained_field="course",
        chained_model_field="course",
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
    course_date_finish = models.DateField(null=True, blank=True)
    enrollment_fee = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)
    course_weekly_price = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)
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
    accommodation_price_list = ChainedForeignKey(
        AccommodationPriceList, 
        chained_field="accommodation",
        chained_model_field="school_accommodation",
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
    accommodation_date_finish = models.DateField(null=True, blank=True)
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
    school_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    accommodation_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    airport_transfer_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    branch = models.ForeignKey(AgencyBranch, on_delete=models.CASCADE, null=True, blank=True)
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(_("status"), choices=QuotationStatus.choices, null=True, blank=True, max_length=255, default="pending")


    def __str__(self):
        return f"#{self.id}"
    
    
    def calculate_school_total(self):
        """
        Calculate the total cost based on course price and number of weeks.
        """
        if self.course_qty_weeks:
            total = self.course_qty_weeks.week_price_ls * self.course_qty_weeks.qty_weeks
        else:
            total = 0
        return total


    def calculate_accommodation_total(self):
        """
        Calculate the total cost based on course price and number of weeks.
        """
        if self.accommodation_qty_weeks:
            total = self.accommodation_qty_weeks.week_price_ls * self.accommodation_qty_weeks.qty_weeks
        else:
            total = 0
        return total
    
    
    def save(self, *args, **kwargs):
        # Calculate the total before saving
        if self.course.enrollment_fee:
            self.enrollment_fee = self.course.enrollment_fee
        else:
            self.enrollment_fee = 0
        self.school_total = self.calculate_school_total()
        self.accommodation_total = self.calculate_accommodation_total()
        if self.airport_transfer:
            self.airport_transfer_total = self.airport_transfer.price
        else:
            self.airport_transfer_total = 0
        self.total = self.school_total + self.accommodation_total + self.airport_transfer_total + self.enrollment_fee
        super(Quotation, self).save(*args, **kwargs)

    
    def delete(self, *args, **kwargs):
        """
        Override the delete method to prevent deletion if status is 'approved'.
        """
        if self.status == QuotationStatus.APPROVED:
            raise ValidationError(_("You cannot delete a quotation that has been approved."))
        super(Quotation, self).delete(*args, **kwargs)

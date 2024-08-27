from django.db import models

from smart_selects.db_fields import ChainedForeignKey

from locations.models import Country, State, City
from enquiries.models import Enquiry
from students.models import StudentProfile
from branches.models import AgencyBranch, EmployeeProfile
from providers.models import (School, Course, CoursePrice, CoursePriceList, SchoolAccommodation, 
    AccommodationPrice, AccommodationPriceList, SchoolAirportTransfer)


class Quotation(models.Model):
    """
    Quotation model representing a student's quote for a course, which can be 
    converted into an Enrollment if method is_enrolled is True.
    """

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
    date_start = models.DateField(null=True, blank=True)
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
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"
    
    
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
        if self.course_qty_weeks:
            total = self.accommodation_qty_weeks.week_price_ls * self.accommodation_qty_weeks.qty_weeks
        else:
            total = 0
        return total
    
    
    def save(self, *args, **kwargs):
        # Calculate the total before saving
        enrollment_fee = self.course.enrollment_fee if self.course.enrollment_fee else 0
        self.total = (
            self.calculate_school_total() +
            self.calculate_accommodation_total() +
            self.airport_transfer.price +
            enrollment_fee
        )
        super().save(*args, **kwargs)



    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)  # Save the Quotation first

    #     if self.is_accepted:
    #         # Create an Enrollment if not already exists for this quotation
    #         enrollment, created = Enrollment.objects.get_or_create(
    #             student=self.student,
    #             program=self.program,
    #             course=self.course,
    #             course_qty_weeks=self.course_qty_weeks,
    #             date_start=self.date_start,
    #             enrollment_fee=self.enrollment_fee,
    #             course_weekly_price=self.course_weekly_price,
    #             accommodation=self.accommodation,
    #             accommodation_qty_weeks=self.accommodation_qty_weeks,
    #             airport_transfer=self.airport_transfer,
    #             total=self.total,
    #             branch=self.branch,
    #             employee=self.employee,
    #         )
    #         if created:
    #             print(f"Enrollment created for {self.student} from Quotation ID {self.id}")
    #     else:
    #         # Delete the associated Enrollment if it exists
    #         try:
    #             enrollment = Enrollment.objects.get(
    #                 student=self.student,
    #                 program=self.program,
    #                 course=self.course,
    #                 course_qty_weeks=self.course_qty_weeks,
    #                 date_start=self.date_start,
    #                 enrollment_fee=self.enrollment_fee,
    #                 course_weekly_price=self.course_weekly_price,
    #                 accommodation=self.accommodation,
    #                 accommodation_qty_weeks=self.accommodation_qty_weeks,
    #                 airport_transfer=self.airport_transfer,
    #                 total=self.total,
    #                 branch=self.branch,
    #                 employee=self.employee,
    #             )
    #             enrollment.delete()
    #             print(f"Enrollment deleted for {self.student} from Quotation ID {self.id}")
    #         except Enrollment.DoesNotExist:
    #             pass  # No associated Enrollment exists, so nothing to delete

    
    
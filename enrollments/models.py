from django.db import models
from branches.models import AgencyBranch, EmployeeProfile
from students.models import StudentProfile
# from quotations.models import Quotation

class Enrollment(models.Model):
    """
    Represents the enrollment of a student, created from a confirmed quotation.
    """

    quotation = models.CharField(max_length=100, blank=True, null=True)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, null=True, blank=True)
    nationality = models.ForeignKey('locations.Country', null=True, blank=True, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    program = models.ForeignKey('providers.School', on_delete=models.CASCADE)
    course = models.ForeignKey('providers.Course', on_delete=models.CASCADE, null=True, blank=True)
    course_qty_weeks = models.ForeignKey('providers.CoursePrice', on_delete=models.CASCADE, null=True, blank=True)
    date_start = models.DateField(null=True, blank=True)
    enrollment_fee = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)
    course_weekly_price = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)
    accommodation = models.ForeignKey('providers.SchoolAccommodation', on_delete=models.CASCADE, null=True, blank=True)
    accommodation_qty_weeks = models.ForeignKey('providers.AccommodationPrice', on_delete=models.CASCADE, null=True, blank=True)
    airport_transfer = models.ForeignKey('providers.SchoolAirportTransfer', null=True, blank=True, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    branch = models.ForeignKey(AgencyBranch, on_delete=models.CASCADE, null=True, blank=True)
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Enrollment for {self.student} ({self.email}) in {self.course}"

    # def save(self, *args, **kwargs):
    #     # Ensure that student and course information from the quotation is retained in the enrollment
    #     if self.quotation:
    #         self.student = self.quotation.student
    #         self.program = self.quotation.program
    #         self.course = self.quotation.course
    #         self.course_qty_weeks = self.quotation.course_qty_weeks
    #         self.date_start = self.quotation.date_start
    #         self.enrollment_fee = self.quotation.enrollment_fee
    #         self.course_weekly_price = self.quotation.course_weekly_price
    #         self.accommodation = self.quotation.accommodation
    #         self.accommodation_qty_weeks = self.quotation.accommodation_qty_weeks
    #         self.airport_transfer = self.quotation.airport_transfer
    #         self.total = self.quotation.total

    #     super().save(*args, **kwargs)

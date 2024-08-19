from django.db import models

from enquiries.models import Enquiry
from students.models import StudentProfile
from branches.models import AgencyBranch, EmployeeProfile
from enrollments.models import Enrollment


class Quotation(models.Model):
    """
    Quotation model representing a student's quote for a course, which can be 
    converted into an Enrollment if method is_enrolled is True.
    """

    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, null=True, blank=True)
    enquiry = models.OneToOneField(Enquiry, on_delete=models.CASCADE, related_name="quotation", null=True, blank=True)
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
    is_enrolled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the Quotation first

        if self.is_enrolled:
            # Create an Enrollment if not already exists for this quotation
            enrollment, created = Enrollment.objects.get_or_create(
                student=self.student,
                program=self.program,
                course=self.course,
                course_qty_weeks=self.course_qty_weeks,
                date_start=self.date_start,
                enrollment_fee=self.enrollment_fee,
                course_weekly_price=self.course_weekly_price,
                accommodation=self.accommodation,
                accommodation_qty_weeks=self.accommodation_qty_weeks,
                airport_transfer=self.airport_transfer,
                total=self.total,
                branch=self.branch,
                employee=self.employee,
            )
            if created:
                print(f"Enrollment created for {self.student} from Quotation ID {self.id}")
from django.db import models
from branches.models import AgencyBranch, EmployeeProfile
from students.models import StudentProfile

class Enrollment(models.Model):
    """
    Needs to be upgrade in de DER
    """

    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, null=True, blank=True)  # Added this line
    nationality = models.ForeignKey('locations.Country', null=True, blank=True, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)  # Added date of birth field
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
        return f"{self.student} ({self.email}) enrolled in {self.course}"

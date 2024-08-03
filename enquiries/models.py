from django.db import models

# Create your models here.


# This is the original inquiry for the programs
class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    program = models.ForeignKey('programs.Experience', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.name} ({self.email})"
    

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
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
    airport_transfer = models.ForeignKey('providers.SchoolAirportTransfer', null=True, blank=True, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # Add branch assigned
    # Add seller assigned
    

    def __str__(self):
        return f"Enquiry from {self.name} ({self.email})"





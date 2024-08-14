from django.db import models
from django.contrib.auth.models import User

from branches.models import AgencyBranch, EmployeeProfile


# Create your models here.

class StudentProfile(models.Model):
    """
    Still need to create a many to many relationship with AgencyBranch.
    """
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    branch = models.ForeignKey(AgencyBranch, on_delete=models.CASCADE, null=True, blank=True)
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname} "
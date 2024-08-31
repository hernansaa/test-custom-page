from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from branches.models import AgencyBranch, EmployeeProfile



class StudentStatus(models.TextChoices):
        ENROLLED = "enrolled", _("Enrolled")
        NOT_ENROLLED = "not enrolled", _("Not enrolled")
        STUDYING = "studying", _("Studying")


class StudentProfile(models.Model):
    """
    Still need to create a many to many relationship with AgencyBranch.
    """
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    status = models.CharField(_("status"), choices=StudentStatus.choices, null=True, blank=True, max_length=255, default="not enrolled")
    branch = models.ForeignKey(AgencyBranch, on_delete=models.CASCADE, null=True, blank=True)
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
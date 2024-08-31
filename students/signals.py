from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import StudentProfile
from enrollments.models import Enrollment


@receiver(post_save, sender=Enrollment)
def update_student_status_to_enrolled(sender, instance, **kwargs):
    # Update the existing Student Profile using the update method
    StudentProfile.objects.filter(id=instance.student.id).update(
        status = "enrolled"
    )


@receiver(post_delete, sender=Enrollment)
def update_student_status_to_not_enrolled(sender, instance, **kwargs):
    # Update the existing Student Profile using the update method
    StudentProfile.objects.filter(id=instance.student.id).update(
        status = "not enrolled"
    )


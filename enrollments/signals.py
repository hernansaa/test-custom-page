from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Enrollment
from invoices.models import Invoice

@receiver(post_save, sender=Invoice)
def create_enrollment(sender, instance, created, **kwargs):
    if instance.enrollment_fee_paid == True:
        # Check if the enrollment already exists for this quotation
        if not hasattr(instance, 'enrollment'):            

            Enrollment.objects.create(
                invoice = instance,
                student = instance.student,
                city = instance.city,
                school = instance.school,
                course = instance.course,
                course_qty_weeks = instance.course_qty_weeks,
                course_date_start = instance.course_date_start,
                accommodation = instance.accommodation,
                accommodation_qty_weeks = instance.accommodation_qty_weeks,
                accommodation_date_start=instance.accommodation_date_start,
                airport_transfer = instance.airport_transfer,
            )
        else:
            # Update the existing enrollment using the update method
            Enrollment.objects.filter(id=instance.enrollment.id).update(
                student = instance.student,
                city = instance.city,
                school=instance.school,
                course=instance.course,
                course_qty_weeks=instance.course_qty_weeks,
                course_date_start=instance.course_date_start,
                accommodation=instance.accommodation,
                accommodation_qty_weeks=instance.accommodation_qty_weeks,
                accommodation_date_start=instance.accommodation_date_start,
                airport_transfer=instance.airport_transfer,
            )



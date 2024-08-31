from celery import shared_task
from django.utils import timezone
from enrollments.models import Enrollment
from students.models import StudentProfile


@shared_task
def update_student_statuses():
    today = timezone.now().date()
    enrollments = Enrollment.objects.all()

    for enrollment in enrollments:
        if enrollment.course_finish_date and enrollment.course_finish_date < today:
            StudentProfile.objects.filter(id=enrollment.student.id).update(status="not enrolled")
        else:
            StudentProfile.objects.filter(id=enrollment.student.id).update(status="enrolled")
            

# @shared_task
# def print_hello():
#     print("Hello! This task runs every 5 seconds.")
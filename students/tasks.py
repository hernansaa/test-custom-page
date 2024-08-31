from celery import shared_task
from django.utils import timezone
from enrollments.models import Enrollment
from students.models import StudentProfile


# Should I consider performing this check everytime the 
# students model invoked in the admin? Just in case Celery Fails? 
@shared_task
def update_student_statuses():
    today = timezone.now().date()
    enrollments = Enrollment.objects.all()

    for enrollment in enrollments:
        if enrollment.course_date_finish and enrollment.course_date_finish < today:
            StudentProfile.objects.filter(id=enrollment.student.id).update(status="not enrolled")
        elif enrollment.course_date_start < today < enrollment.course_date_finish:
            StudentProfile.objects.filter(id=enrollment.student.id).update(status="studying")
        else:
            StudentProfile.objects.filter(id=enrollment.student.id).update(status="enrolled")




# @shared_task
# def print_hello():
#     print("Hello! This task runs every 5 seconds.")
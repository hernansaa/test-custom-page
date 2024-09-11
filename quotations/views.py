from django.shortcuts import render, get_object_or_404
from .models import Quotation
from providers.models import School, Course
from students.models import StudentProfile

from .forms import QuotationAdminForm

# Create your views here.

def update_quotation(request, id):
  
  quotation = get_object_or_404(Quotation, id=id)
  
  if request.method == "POST":
        form = QuotationAdminForm(request.POST, instance=quotation)
        if form.is_valid():
            form.save()
  else:
      form = QuotationAdminForm()  # Create an empty form for GET requests

  context = {
    'quotation': quotation,
  }

  return render(request, 'quotations/updated-quotation.html', context)




# def update_quotation(request, id):
  
#   if request.method == 'POST':
#   quotation = get_object_or_404(Quotation, id=id)
#   student_id = request.POST.get('student')
#   student = get_object_or_404(StudentProfile, id=student_id)
#   school_id = request.POST.get('school')
#   school = get_object_or_404(School, id=school_id)
#   course_id = request.POST.get('course')
#   course = get_object_or_404(Course, id=course_id)
#   course_qty_weeks = str(request.POST.get('course_qty_weeks'))
#   # course_qty_weeks = get_object_or_404(Quotation, id=course_qty_weeks_id)

#   context = {
#     'quotation': quotation,
#     'student': student,
#     'school': school,
#     'course': course,
#     'course_qty_weeks': course_qty_weeks,
#   }

#   return render(request, 'quotations/updated-quotation.html', context)
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Quotation
from students.models import StudentProfile
from providers.models import (
  School, 
  Course, 
  CoursePrice, 
  AccommodationPrice, 
  SchoolAccommodation,
  SchoolAirportTransfer
  )

from .forms import QuotationAdminForm


def update_quotation(request, id):
  
  if request.method == 'POST':
    quotation = get_object_or_404(Quotation, id=id)
    student_id = request.POST.get('student')
    student = get_object_or_404(StudentProfile, id=student_id)
    school_id = request.POST.get('school')
    school = get_object_or_404(School, id=school_id)
    course_id = request.POST.get('course')
    course = get_object_or_404(Course, id=course_id)
    course_price_id = request.POST.get('course_qty_weeks')
    course_price = get_object_or_404(CoursePrice, id=course_price_id)
    course_date_start = request.POST.get('course_date_start')
    course_date_finish = request.POST.get('course_date_finish')
    accommodation_id = request.POST.get('accommodation')
    accommodation = get_object_or_404(SchoolAccommodation, id=accommodation_id)
    accommodation_price_id = request.POST.get('accommodation_qty_weeks')
    accommodation_price = get_object_or_404(AccommodationPrice, id=accommodation_price_id)
    accommodation_date_start = request.POST.get('accommodation_date_start')
    accommodation_date_finish = request.POST.get('accommodation_date_finish')
    airport_transfer_id = request.POST.get('airport_transfer')
    airport_transfer = get_object_or_404(SchoolAirportTransfer, id=airport_transfer_id)
    status = request.POST.get('status')

  quotation_total = (
    course.enrollment_fee + 
    airport_transfer.price +
    accommodation_price.week_price_ls * accommodation_price.qty_weeks +
    course_price.week_price_ls * course_price.qty_weeks
    )
  
  context = {
    'quotation': quotation,
    'student': student,
    'school': school,
    'course': course,
    'course_price': course_price,
    'course_date_start': course_date_start,
    'course_date_finish': course_date_finish,
    'accommodation': accommodation,
    'accommodation_price': accommodation_price,
    'accommodation_date_start': accommodation_date_start,
    'accommodation_date_finish': accommodation_date_finish,
    'airport_transfer': airport_transfer,
    'quotation_total': quotation_total,
    'status': status,
  }

  return render(request, 'admin/quotations/partials/_updated-quotation.html', context)



# # This a clean code solution but it updates the quotation on every change
# # not sure this is what we want.

# def update_quotation(request, id):
  
#   quotation = get_object_or_404(Quotation, id=id)
  
#   if request.method == "POST":
#         form = QuotationAdminForm(request.POST, instance=quotation)
#         if form.is_valid():
#             form.save()
#   else:
#       form = QuotationAdminForm()  # Create an empty form for GET requests

#   context = {
#     'quotation': quotation,
#   }

#   return render(request, 'admin/quotations/partials/_updated-quotation.html', context)


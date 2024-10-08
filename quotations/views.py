from django.shortcuts import render, get_object_or_404

from .models import Quotation
from students.models import StudentProfile
from providers.models import (
  School, 
  Course, 
  CoursePrice, 
  CoursePriceList,
  AccommodationPrice,
  SchoolAccommodation,
  SchoolAirportTransfer
  )

from .forms import QuotationAdminForm


def update_quotation(request, id):
    # Initialize variables
    quotation = get_object_or_404(Quotation, id=id)
    student = None
    school = None
    course = None
    course_price = None
    course_date_start = None
    course_date_finish = None
    accommodation = None
    accommodation_price = None
    accommodation_date_start = None
    accommodation_date_finish = None
    airport_transfer = None
    status = None

    if request.method == 'POST':
        student_id = request.POST.get('student')
        if student_id:
            student = get_object_or_404(StudentProfile, id=student_id)
        
        school_id = request.POST.get('school')
        if school_id:
            school = get_object_or_404(School, id=school_id)
        
        course_id = request.POST.get('course')
        if course_id:
            course = get_object_or_404(Course, id=course_id)
        
        course_price_id = request.POST.get('course_qty_weeks')
        if course_price_id:
            course_price = get_object_or_404(CoursePrice, id=course_price_id)
        
        course_date_start = request.POST.get('course_date_start')
        course_date_finish = request.POST.get('course_date_finish')
        
        accommodation_id = request.POST.get('accommodation')
        if accommodation_id:
            accommodation = get_object_or_404(SchoolAccommodation, id=accommodation_id)
        
        accommodation_price_id = request.POST.get('accommodation_qty_weeks')
        if accommodation_price_id:
            accommodation_price = get_object_or_404(AccommodationPrice, id=accommodation_price_id)
        
        accommodation_date_start = request.POST.get('accommodation_date_start')
        accommodation_date_finish = request.POST.get('accommodation_date_finish')
        
        airport_transfer_id = request.POST.get('airport_transfer')
        if airport_transfer_id:
            airport_transfer = get_object_or_404(SchoolAirportTransfer, id=airport_transfer_id)
        
        # Calculate total if all necessary data is present
        if course and airport_transfer and accommodation_price and course_price:
            quotation_total = (
                course.enrollment_fee +
                airport_transfer.price +
                accommodation_price.week_price_ls * accommodation_price.qty_weeks +
                course_price.week_price_ls * course_price.qty_weeks
            )
        else:
            quotation_total = 0
    else:
        # Handle GET request case if needed
        # For instance, you might want to set some default values or just pass existing data
        pass
    
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

    return render(request, 'admin/quotations/partials/_updated_quotation.html', context)



def get_schools_by_city(request, id):
    quotation = get_object_or_404(Quotation, id=id)
    city_id = request.POST.get('city')

    if request.GET.get('trigger') == 'load':
        template = 'admin/quotations/partials/_schools_options_on_load.html'
    else:
        template = 'admin/quotations/partials/_schools_options_on_change.html'

    # Fetch schools based on the school ID
    if city_id:
        schools = School.objects.filter(address__city=city_id)
    else:
        schools = School.objects.none()  # No schools available if no school ID

    context = {
        'schools': schools,
        'quotation': quotation,
    }

    return render(request, template, context)


def get_courses_by_school(request, id):
    quotation = get_object_or_404(Quotation, id=id)
    school_id = request.POST.get('school')

    if request.GET.get('trigger') == 'load':
        template = 'admin/quotations/partials/_courses_dropdown_on_load.html'
    else:
        template = 'admin/quotations/partials/_courses_dropdown_on_change.html'

    # Fetch courses based on the school ID
    if school_id:
        courses = Course.objects.filter(school=school_id)
    else:
        courses = Course.objects.none()  # No courses available if no school ID

    context = {
        'courses': courses,
        'quotation': quotation,
    }

    return render(request, template, context)


def get_price_lists_by_course(request, id):
    quotation = get_object_or_404(Quotation, id=id)
    course_id = request.POST.get('course')

    # Determine the correct template to render based on the trigger
    if request.GET.get('trigger') == 'load':
        template = 'admin/quotations/partials/_price_lists_dropdown_on_load.html'
    else:
        template = 'admin/quotations/partials/_price_lists_dropdown_on_change.html'

    
    if course_id:
      course_price_lists = CoursePriceList.objects.filter(course=course_id)
    else:
      course_price_lists = {} 
        
    context = {
       'course_price_lists': course_price_lists,
       'quotation': quotation,
    }

    return render(request, template, context)


def get_course_prices_by_price_list(request, id):
    quotation = get_object_or_404(Quotation, id=id)
    course_price_list_id = request.POST.get('course_price_list')

    # Determine the correct template to render based on the trigger
    if request.GET.get('trigger') == 'load':
        template = 'admin/quotations/partials/_course_prices_dropdown_on_load.html'
    else:
        template = 'admin/quotations/partials/_course_prices_dropdown_on_change.html'
    
    if course_price_list_id:
      course_prices = CoursePrice.objects.filter(course_price_list=course_price_list_id)
    else:
      course_prices = {}

    context = {
       'course_prices': course_prices,
       'quotation': quotation,
    }

    return render(request, template, context)










# # This a clean code solution for updating the quotation
# # but it updates the quotation on every change
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


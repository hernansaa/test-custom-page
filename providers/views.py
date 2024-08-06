from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import JsonResponse

from .models import (School, Address, SchoolAccommodation, SchoolAirportTransfer, SchoolExtra, 
                     SchoolAvgAge, SchoolClassroomEquipment, NationalityMix, Course, CoursePrice, AccommodationPrice)

from locations.models import Country

from enquiries.forms import EnquiryForm
from enquiries.models import Enquiry

# Create your views here.


def index(request):
    
    schools = School.objects.prefetch_related('address_set').all()
    countries = Country.objects.all()
    addresses = Address.objects.all()
    
    context = {
        'schools': schools,
        'countries': countries,
        'addresses': addresses,
    }
    
    return render(request, 'providers/index.html', context)


def school_details(request, pk):
    # Retrieve the school object based on the pk from URL
    school = get_object_or_404(School, pk=pk)
    school_accommodations = SchoolAccommodation.objects.filter(school=school)
    school_airport_transfers = SchoolAirportTransfer.objects.filter(school=school)
    school_extras = SchoolExtra.objects.filter(school=school)
    school_avg_ages = SchoolAvgAge.objects.filter(school=school)
    school_classroom_equipments = SchoolClassroomEquipment.objects.filter(school=school)
    nationality_mixes = NationalityMix.objects.filter(school=school)
    courses = Course.objects.filter(school=school)

    if request.method == 'POST':
        form = EnquiryForm(request.POST, school_id=pk)

        course_id = request.POST.get('course')
        accommodation_id = request.POST.get('accommodation')
        
        if course_id:
            # course = get_object_or_404(Course, id=course_id)
            # form.fields['course_qty_weeks'].queryset = CoursePrice.objects.filter(course_id=course_id)
            
            course = Course.objects.get(id=course_id)
            form.fields['course_qty_weeks'].queryset = CoursePrice.objects.filter(course_price_list__course=course)
            form.fields['enrollment_fee'].initial= course.enrollment_fee
    
        if accommodation_id:
            school_accommodation = SchoolAccommodation.objects.get(id=accommodation_id)
            form.fields['accommodation_qty_weeks'].queryset = AccommodationPrice.objects.filter(accommodation_price_list__school_accommodation=school_accommodation)

        if form.is_valid():
            # Create a new Inquiry object but don't save it yet
            enquiry = Enquiry(
                name=form.cleaned_data['name'],
                dob=form.cleaned_data['dob'],
                nationality=form.cleaned_data['nationality'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                program=school,  # Assign the program/experience to the inquiry
                enrollment_fee=form.cleaned_data['enrollment_fee'],
                accommodation=form.cleaned_data['accommodation'],
                course=form.cleaned_data['course'],
                date_start=form.cleaned_data['date_start'],
                course_weekly_price=form.cleaned_data['course_weekly_price'],
                course_qty_weeks=form.cleaned_data['course_qty_weeks'],
                accommodation_qty_weeks=form.cleaned_data['accommodation_qty_weeks'],
                total=form.cleaned_data['total'],
            )
            enquiry.save()
            # Optionally, we can redirect to a success page or clear the form
            return redirect('school-details', pk=pk)  # Redirect to the same page or another success page
        else:
            form_errors = form.errors
    else:
        form = EnquiryForm(school_id=pk)
        form.fields['course'].queryset = Course.objects.filter(school=pk)
        form.fields['accommodation'].queryset = SchoolAccommodation.objects.filter(school=pk)
        form.fields['airport_transfer'].queryset = SchoolAirportTransfer.objects.filter(school=pk)
        form_errors = None

    context = {
        'school': school,
        'school_accommodations': school_accommodations,
        'school_airport_transfers': school_airport_transfers,
        'school_extras': school_extras,
        'school_avg_ages': school_avg_ages,
        'school_classroom_equipments': school_classroom_equipments,
        'nationality_mixes': nationality_mixes,
        'courses': courses,
        'form': form,
        'form_errors': form_errors,
    }

    return render(request, 'providers/school-details.html', context)


def update_course_price(request):
    # Initialize the form with POST data if available
    form = EnquiryForm(request.POST or None)
    
    course_id = request.POST.get('course')
    
    if course_id:
        # course = get_object_or_404(Course, id=course_id)
        # course_price = CoursePrice.objects.filter(course_id=course_id)
        
        # # Update the queryset for the 'course_qty_weeks' field
        # form.fields['course_qty_weeks'].queryset = course_price

        course = Course.objects.get(id=course_id)
        form.fields['course_qty_weeks'].queryset = CoursePrice.objects.filter(course_price_list__course=course)
        form.fields['enrollment_fee'].initial= course.enrollment_fee
        
        # Set the initial value of 'enrollment_fee'
        form.fields['enrollment_fee'].initial = course.enrollment_fee

        context = {
            'form': form,
        }

        return render(request, 'providers/partials/_course_price_fragment.html', context)
    else:
        return JsonResponse({'error': 'Invalid course ID'}, status=400)


def update_accommodation_price(request):

    form = EnquiryForm(request.POST or None)
    
    accommodation_id = request.POST.get('accommodation')
    
    if accommodation_id:
        school_accommodation = SchoolAccommodation.objects.get(id=accommodation_id)
        accommodation_price_list = AccommodationPrice.objects.filter(accommodation_price_list__school_accommodation=school_accommodation)
        form.fields['accommodation_qty_weeks'].queryset = accommodation_price_list

        return render(request, 'providers/partials/_accommodation_price_fragment.html', {'form': form})
    else:
        return JsonResponse({'error': 'Invalid course ID'}, status=400)


def update_total_price(request):
    form = EnquiryForm()

    total = 0
    
    course = 'Curso'
    course_qty_weeks = 0
    course_price = 0
    course_enrollment_fee = 0
    course_total = 0
    
    accommodation_total = 0
    accommodation_qty_weeks = 0
    accommodation_week_price_ls = 0
    school_accommodation = 'alojamiento'

    school_airport_transfer = 'Sin traslado aeropuerto'
    school_airport_transfer_price = 0

    course_id = request.POST.get('course')
    if course_id:
        course = get_object_or_404(Course, id=course_id)
        course_enrollment_fee = course.enrollment_fee
    
    course_qty_weeks_id = request.POST.get('course_qty_weeks')
    if course_qty_weeks_id:
        course_price_obj = get_object_or_404(CoursePrice, course_price_list__course=course_id, qty_weeks=course_qty_weeks_id)
        course_price = course_price_obj.week_price_ls
        course_qty_weeks = course_price_obj.qty_weeks
        course_total = course_price * course_qty_weeks
    total += course_total + course_enrollment_fee

    accommodation_id = request.POST.get('accommodation')
    if accommodation_id:
        school_accommodation = get_object_or_404(SchoolAccommodation, id=accommodation_id)
        accommodation_qty_weeks_id = request.POST.get('accommodation_qty_weeks')
        if accommodation_qty_weeks_id:
            accommodation_price_obj = get_object_or_404(AccommodationPrice, accommodation_price_list__school_accommodation=school_accommodation, qty_weeks=accommodation_qty_weeks_id)
            accommodation_qty_weeks = accommodation_price_obj.qty_weeks
            accommodation_week_price_ls = accommodation_price_obj.week_price_ls
            accommodation_total = accommodation_qty_weeks * accommodation_week_price_ls
        total += accommodation_total

    airport_transfer_id = request.POST.get('airport_transfer')
    if airport_transfer_id:
        school_airport_transfer = get_object_or_404(SchoolAirportTransfer, id=airport_transfer_id)
        school_airport_transfer_price = school_airport_transfer.price
        total += school_airport_transfer_price

    form.fields['total'].initial = total

    context = {
        'course': course,
        'course_qty_weeks': course_qty_weeks,
        'course_price': course_price,
        'course_enrollment_fee': course_enrollment_fee,
        'course_total': course_total,
        'school_accommodation': school_accommodation,
        'accommodation_qty_weeks': accommodation_qty_weeks,
        'accommodation_week_price_ls': accommodation_week_price_ls,
        'accommodation_total': accommodation_total,
        'school_airport_transfer': school_airport_transfer,
        'school_airport_transfer_price': school_airport_transfer_price,
        'total': total,
        'form': form,
    }
    
    return render(request, 'providers/partials/_total_price_fragment.html', context)


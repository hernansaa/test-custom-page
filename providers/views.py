from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from .models import (School, Address, SchoolAccommodation, SchoolAirportTransfer, SchoolExtra, 
                     SchoolAvgAge, SchoolClassroomEquipment, NationalityMix, Course)

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
                qty_weeks=form.cleaned_data['qty_weeks'],
                total=form.cleaned_data['total'],
            )
            enquiry.save()
            # Optionally, we can redirect to a success page or clear the form
            return redirect('school-details', pk=pk)  # Redirect to the same page or another success page
    else:
        form = EnquiryForm(school_id=pk)
        form.fields['course'].queryset = Course.objects.filter(school=pk)
        form.fields['accommodation'].queryset = SchoolAccommodation.objects.filter(school=pk)
        form.fields['airport_transfer'].queryset = SchoolAirportTransfer.objects.filter(school=pk)


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
    }
    
    return render(request, 'providers/school-details.html', context)


def update_course_price(request):
    course_id = request.POST.get('course')
    if course_id:
        course = get_object_or_404(Course, id=course_id)
        form = EnquiryForm()
        form.fields['course_weekly_price'].initial = course.ls_week_price
        return render(request, 'providers/partials/_course_price_fragment.html', {'form': form})
    return JsonResponse({'error': 'Invalid course ID'}, status=400)


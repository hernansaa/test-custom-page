from django.shortcuts import render, redirect, get_object_or_404
from .models import Experience, CourseType
from locations.models import Country

from django.http import JsonResponse

from providers.models import School, Course

from enquiries.forms import InquiryForm
from enquiries.models import Inquiry

def index(request): 
    
    experiences = Experience.objects.all()
    countries = Country.objects.all()
    course_types = CourseType.objects.all()
    
    context = {
        'experiences': experiences,
        'countries': countries,
        'course_types': course_types,
    }
    
    return render(request, 'programs/index.html', context)


def filter_options_by_country(request):
    country_filter = request.GET.get("country_filter")

    if country_filter:
        # Filtering course types based on the selected country
        course_types = CourseType.objects.filter(
            experience__city__state__country__id=country_filter
        ).distinct()
    else:
        course_types = CourseType.objects.all()

    countries = Country.objects.all()

    context = {
        'countries': countries,
        'course_types': course_types,
    }

    return render(request, 'programs/partials/_options_filtered.html', context)


def results_filtered(request):
    country_filter = request.GET.get("country_filter")
    course_type_filter = request.GET.get("course_type_filter")

    experiences = Experience.objects.all()
    
    if country_filter:
        experiences = experiences.filter(city__state__country__id=country_filter)
        
    if course_type_filter:
        experiences = experiences.filter(course_type__id=course_type_filter)

    context = {
        'experiences': experiences,
    }
    
    return render(request, 'programs/partials/_results_filtered.html', context)


def program_details(request, pk):
    
    # Retrieve the Experience object based on the pk from URL
    experience = get_object_or_404(Experience, pk=pk)

    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            # Create a new Inquiry object but don't save it yet
            inquiry = Inquiry(
                name=form.cleaned_data['name'],
                nationality=form.cleaned_data['nationality'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                program=experience  # Assign the program/experience to the inquiry
            )
            inquiry.save()
            # Optionally, you can redirect to a success page or clear the form
            return redirect('program-details', pk=pk)  # Redirect to the same page or another success page
    else:
        form = InquiryForm()

    context = {
        'experience': experience,
        'form': form,
    }
    
    return render(request, 'programs/program-details.html', context)



def filter_courses(request):
    school_id = request.POST.get('school_id')
    courses = Course.objects.filter(school_id=school_id).values('id', 'name')
    return JsonResponse(list(courses), safe=False)

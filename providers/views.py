from django.shortcuts import render, redirect, get_object_or_404

from .models import School, Address, SchoolAccommodation, SchoolAirportTransfer, SchoolExtra

from locations.models import Country, City

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
    
    # Retrieve the Experience object based on the pk from URL
    school = get_object_or_404(School, pk=pk)
    school_accommodations = SchoolAccommodation.objects.filter(school=school)
    school_airport_transfer = SchoolAirportTransfer.objects.filter(school=school)
    school_extra = SchoolExtra.objects.filter(school=school)


    # if request.method == 'POST':
    #     form = InquiryForm(request.POST)
    #     if form.is_valid():
    #         # Create a new Inquiry object but don't save it yet
    #         inquiry = Inquiry(
    #             name=form.cleaned_data['name'],
    #             nationality=form.cleaned_data['nationality'],
    #             email=form.cleaned_data['email'],
    #             phone=form.cleaned_data['phone'],
    #             program=experience  # Assign the program/experience to the inquiry
    #         )
    #         inquiry.save()
    #         # Optionally, you can redirect to a success page or clear the form
    #         return redirect('program-details', pk=pk)  # Redirect to the same page or another success page
    # else:
    #     form = InquiryForm()

    context = {
        'school': school,
        'school_accommodations': school_accommodations,
        'school_airport_transfer': school_airport_transfer,
        # 'form': form,
    }
    
    return render(request, 'providers/school-details.html', context)
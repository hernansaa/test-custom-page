from django.shortcuts import render

from .models import School
from locations.models import Country, City

# Create your views here.


def index(request):
    
    schools = School.objects.all()
    countries = Country.objects.all()
    cities = City.objects.all()
    
    context = {
        'experiences': schools,
        'countries': countries,
        'cities': cities,

    }
    
    return render(request, 'providers/index.html', context)
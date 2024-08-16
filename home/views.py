from django.shortcuts import render

from .models import AboutUs

# Create your views here.

def index(request):
    return render(request, 'home/index.html')


def contact(request):
    return render(request, 'home/contact.html')


def about_us(request):
    about_us_page = AboutUs.objects.prefetch_related('team_members').first()
    return render(request, 'home/about_us.html', {'about_us_page': about_us_page})

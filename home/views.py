from django.shortcuts import render, redirect

from .models import AboutUs, ContactPage

from .models import StudentReviewsSection, WhyUsSection, ContactSection
from branches.models import AgencyBranch
from enquiries.forms import ContactForm

# Create your views here.

def index(request):
    student_review_section = StudentReviewsSection.objects.all()
    why_us_section = WhyUsSection.objects.all()
    contact_section = ContactSection.objects.first()
    
    context = {
        'student_review_section': student_review_section,
        'why_us_section': why_us_section,
        'contact_section': contact_section
    }

    return render(request, 'home/index.html', context)


def contact(request):
    contact_page = ContactPage.objects.first()
    agency_branches = AgencyBranch.objects.all()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_page')

    context = {
        'contact_page': contact_page,
        'agency_branches': agency_branches,
        'form': form,
    }

    return render(request, 'home/contact.html', context)


def about_us(request):
    about_us_page = AboutUs.objects.prefetch_related('team_members').first()
    return render(request, 'home/about_us.html', {'about_us_page': about_us_page})

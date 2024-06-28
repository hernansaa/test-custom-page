from django.shortcuts import render, redirect, get_object_or_404
from .forms import InquiryForm
from .models import Inquiry
from programs.models import Experience

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
    return render(request, 'program_details.html', context)
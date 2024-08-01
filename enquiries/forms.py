from django import forms
from .models import Enquiry
from providers.models import Course, School, SchoolAccommodation, SchoolAirportTransfer
from locations.models import Country

from datetime import datetime


class InquiryForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    nationality = forms.CharField(label='Nationality', required=False)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Phone Number', required=False)


class EnquiryForm(forms.ModelForm):
    
    class Meta:
        model = Enquiry
        fields = ['course', 'course_weekly_price', 'qty_weeks', 'date_start', 'enrollment_fee', 'total',
                  'accommodation', 'airport_transfer', 'name', 'nationality', 'dob', 'email', 'phone']
    
    course = forms.ModelChoiceField(queryset=Course.objects.none(), required=False, label='Curso')
    course_weekly_price = forms.DecimalField(label='Precio semanal', initial=200, disabled=True)
    qty_weeks = forms.IntegerField(label='Semanas', initial=2, required=True)
    date_start = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'min': datetime.now().date()}), label='Fecha Inicio')
    #enrollment_fee = forms.DecimalField(label='Matrícula', initial=90, disabled=True)  # Campo de solo lectura
    accommodation = forms.ModelChoiceField(queryset=SchoolAccommodation.objects.none(), label='Alojamiento')
    airport_transfer = forms.ModelChoiceField(queryset=SchoolAirportTransfer.objects.all(), required=False, label='Traslado Aeropuerto')
    name = forms.CharField(label='Nombre', max_length=100)
    nationality = forms.ModelChoiceField(queryset=Country.objects.all(), required=False, label='Nacionalidad')
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'max': datetime.now().date()}), label='Fecha Nacimiento')
    email = forms.EmailField(label='E-mail')
    phone = forms.CharField(label='Teléfono', required=False)

    def __init__(self, *args, **kwargs):
        school_id = kwargs.pop('school_id', None)
        super().__init__(*args, **kwargs)
        if school_id is not None:
            self.fields['course'].queryset = Course.objects.filter(school=school_id)
            self.fields['accommodation'].queryset = SchoolAccommodation.objects.filter(school=school_id)
            self.fields['airport_transfer'].queryset = SchoolAirportTransfer.objects.filter(school=school_id)


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=255, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
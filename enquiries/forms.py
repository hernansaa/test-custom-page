from django import forms
from .models import Enquiry, Contact
from providers.models import Course, School, SchoolAccommodation, SchoolAirportTransfer, CoursePrice, AccommodationPrice, AccommodationPriceList
from locations.models import Country

from datetime import datetime


class InquiryForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    nationality = forms.CharField(label='Nationality', required=False)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Phone Number', required=False)


class EnquiryForm(forms.ModelForm):
    """
    A form for handling enquiries, dynamically populated based on school and course selection.
    """
    
    class Meta:
        model = Enquiry
        fields = ['course', 'course_weekly_price', 'course_qty_weeks', 'date_start', 'enrollment_fee', 'total',
                  'accommodation', 'accommodation_qty_weeks', 'airport_transfer', 'name','surname', 'nationality', 'dob', 
                  'email', 'phone']
    
    course = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=Course.objects.none(), required=False, label='Curso', blank=False, empty_label=None)
    course_weekly_price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label='Precio (semanal)', initial=0, disabled=True)
    course_qty_weeks = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=CoursePrice.objects.none(), required=False, label='Semanas', to_field_name='qty_weeks', empty_label=None)
    date_start = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'min': datetime.now().date()}), label='Fecha Inicio')
    enrollment_fee = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'hidden'}), label='Matrícula', disabled=True)
    total = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'hidden'}))
    accommodation = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=SchoolAccommodation.objects.none(), label='Alojamiento', empty_label='¿Necesitas alojamiento?')
    accommodation_qty_weeks = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=AccommodationPrice.objects.none(), required=False, to_field_name='qty_weeks', label='Semanas Alojamiento', empty_label='¿Cuantas Semanas?')
    airport_transfer = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=SchoolAirportTransfer.objects.all(), required=False, label='Traslado Aeropuerto', empty_label='¿Traslado Aeropuerto?')
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Nombre', max_length=100)
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Apellido', max_length=100)
    nationality = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=Country.objects.all(), required=False, label='Nacionalidad')
    dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'max': datetime.now().date()}), label='Fecha Nacimiento')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='E-mail')
    phone = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label='Teléfono', required=False)

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with optional school_id and course_id.
        - school_id: Used to filter course, accommodation, and airport transfer options.
        - course_id: Used to filter course_qty_weeks and set the initial enrollment fee.
        """
        school_id = kwargs.pop('school_id', None)
        # course_id = kwargs.pop('course_id', None)
        # accommodation_id = kwargs.pop('accommodation_id', None)
        super().__init__(*args, **kwargs)
        self.populate_dynamic_fields(school_id)        
    
    def populate_dynamic_fields(self, school_id):
        """
        Populates form fields dynamically based on the given school_id and course_id.
        
        - If school_id is provided, filter the queryset of the course, accommodation, and airport_transfer fields.
        - If course_id is provided, filter the queryset of the course_qty_weeks field and set the initial value for the enrollment_fee field.
        
        Args:
            school_id (int or None): The ID of the school to filter related fields.
            course_id (int or None): The ID of the course to filter related fields and set initial values.
        """

        if school_id is not None:
            self.fields['course'].queryset = Course.objects.filter(school=school_id)
            self.fields['accommodation'].queryset = SchoolAccommodation.objects.filter(school=school_id)
            self.fields['airport_transfer'].queryset = SchoolAirportTransfer.objects.filter(school=school_id)
        
        # if course_id is not None:
        #     #self.fields['course_qty_weeks'].queryset = CoursePrice.objects.all()
        #     self.fields['enrollment_fee'].initial = Course.objects.filter(course_id=course_id)
        
        # if accommodation_id is not None:
        #     # Get a specific SchoolAccommodation instance
        #     school_accommodation = SchoolAccommodation.objects.get(id=accommodation_id)

        #     # # Access related AccommodationPriceList instances
        #     # price_lists = school_accommodation.accommodationpricelist_set.all()

        #     # Access related AccommodationPrice instances through AccommodationPriceList
        #     self.fields['accommodation_qty_weeks'].queryset = AccommodationPrice.objects.filter(accommodation_price_list__school_accommodation=school_accommodation)



class EmailForm(forms.Form):
    subject = forms.CharField(max_length=255, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'nationality', 'email', 'phone', 'message',]
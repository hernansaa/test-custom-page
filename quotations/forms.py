from django import forms
from .models import Quotation
from datetime import datetime
from providers.models import Course

class QuotationAdminForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = ('__all__')

    course_date_start = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': datetime.now().date()}),
        label='Fecha Inicio'
    )
    course_date_finish = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': datetime.now().date()}),
        label='Fecha Finalizacion'
    )
    accommodation_date_start = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': datetime.now().date()}),
        label='Fecha Inicio'
    )
    accommodation_date_finish = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': datetime.now().date()}),
        label='Fecha Finalizacion'
    )

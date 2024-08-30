from django import forms

from .models import School
from quotations.models import Quotation

class SchoolAdminForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = "__all__"
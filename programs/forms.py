from django import forms

from .models import Experience

class TestAdminForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'

        
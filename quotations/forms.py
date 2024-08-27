from django import forms
from .models import Quotation

class QuotationAdminForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course_qty_weeks'].widget.attrs.update({
            'onchange': 'this.form.submit();'
        })

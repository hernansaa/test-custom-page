from django import forms

class InquiryForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    nationality = forms.CharField(label='Nationality', required=False)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Phone Number', required=False)


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=255, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
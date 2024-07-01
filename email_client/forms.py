from django import forms

class EmailReplyForm(forms.Form):
    subject = forms.CharField(max_length=255, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class ComposeEmailForm(forms.Form):
    recipient = forms.EmailField(label='Recipient')
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)



from django import forms

from django.core.mail import send_mail


class EmailReplyForm(forms.Form):
    subject = forms.CharField(max_length=255, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

"""
    def send_reply(self, sender_email, recipient_email):
        subject = self.cleaned_data['subject']
        body = self.cleaned_data['body']
        from_email = sender_email  # Use the sender's email configured in Django settings
        recipient_list = [recipient_email]
        
        # Send the email using Django's send_mail function
        send_mail(subject, body, from_email, recipient_list, fail_silently=False)
"""
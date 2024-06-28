from django.contrib import admin

from django.core.mail import send_mail

from .models import SentEmail, Message, MessageAttachment

from django.shortcuts import render, redirect
from django.urls import path


from .forms import EmailReplyForm

class SentEmailAdmin(admin.ModelAdmin):
    list_display = ['subject', 'recipient', 'sent_at']
    search_fields = ['subject', 'recipient']
    list_filter = ['sent_at']



# Extended from django-mailbox through Proxy Models


class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'from_header', 'to_header', 'outgoing', 'processed', 'read')
    list_filter = ('outgoing', 'processed', 'read')
    search_fields = ('subject', 'from_header', 'to_header', 'body')

    actions = ['send_email_action']


    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('send-email/', self.admin_site.admin_view(self.send_email_view), name='send-email')
        ]
        return custom_urls + urls


    def send_email_action(self, request, queryset):
        selected = request.POST.getlist('_selected_action')
        return redirect(f'send-email/?ids={",".join(selected)}')


    def send_email_view(self, request):
        if 'apply' in request.POST:
            form = EmailReplyForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                message_template = form.cleaned_data['message']
                from_email = 'hernan@globalstudies.es'

                messages_ids = request.POST.getlist('ids')
                inquiries = Message.objects.filter(id__in=messages_ids)

                for inquiry in inquiries:
                    personalized_message = message_template.format(inquiry.from_header)
                    try:
                        send_mail(subject, personalized_message, from_email, [inquiry.from_header])

                        # Save the sent email details to the database
                        SentEmail.objects.create(
                            subject=subject,
                            message=personalized_message,
                            recipient=inquiry.from_header
                        )
                    
                    except Exception as e:
                        self.message_user(request, f"Failed to send email to {inquiry.email}. Error: {str(e)}", level='error')
                        return redirect('..')

                self.message_user(request, "Emails successfully sent to selected inquiries.")
                return redirect('..')
        else:
            form = EmailReplyForm()
            messages_ids = request.GET.get('ids', '').split(',')
            inquiries = Message.objects.filter(id__in=messages_ids)

        return render(
            request,
            'admin/send_email.html',
            context={'form': form, 'inquiries': inquiries, 'ids': ','.join(messages_ids)}
        )



# Customize admin for CustomMessage
class MessageAttachmentAdmin(admin.ModelAdmin):
    pass


# Register your models with their respective admin classes
admin.site.register(SentEmail, SentEmailAdmin)

# Register the proxy models 
admin.site.register(Message, MessageAdmin)
admin.site.register(MessageAttachment, MessageAttachmentAdmin)



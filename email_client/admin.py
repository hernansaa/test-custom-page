from django.contrib import admin, messages
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.urls import path

from .models import SentEmail, ComposeEmail, Message, MessageAttachment
from .forms import EmailReplyForm


class SentEmailAdmin(admin.ModelAdmin):
    list_display = ['subject', 'recipient', 'sent_at']
    search_fields = ['subject', 'recipient']
    list_filter = ['sent_at']

    def save_model(self, request, obj, form, change):

        try:
            # Send the email before saving the model
            subject = 'A new instance has been saved'
            message = f'A new instance of has been saved:\n\nName: '
            from_email = 'hernan@globalstudies.es'
            recipient_list = ['hernansaa88@gmail.com']  # You can add more recipients here
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, 'Email sent successfully.')
        except Exception as error:
            messages.error(request, f'An error occurred: {error}')
        
        # It shoould be saved if the email was sent (I leave it like that now)
        super().save_model(request, obj, form, change)


# Extended from django-mailbox through Proxy Models

class MessageAttachmentInline(admin.TabularInline):
    model = MessageAttachment
    extra = 0


class MessageAdmin(admin.ModelAdmin):
    
    inlines = [
        MessageAttachmentInline,
    ]

    list_display = (
        'subject',
        'processed',
        'read',
        'mailbox',
        'outgoing',
        #'attachment_count',
    )

    ordering = ['-processed']

    list_filter = (
        'mailbox',
        'outgoing',
        'processed',
        'read',
    )
    exclude = (
        'body',
        'in_reply_to',
    )
    raw_id_fields = (
        'in_reply_to',
    )
    readonly_fields = (
        'message_id',
        'from_header',
        'to_header',
        'subject',
        'processed',
        'read',
        'mailbox',
        'outgoing',
        'text',
    )
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
                from_email = settings.EMAIL_HOST_USER

                messages_ids = request.POST.getlist('ids')
                inquiries = Message.objects.filter(id__in=messages_ids)

                for inquiry in inquiries:
                    personalized_message = message_template.format(inquiry.from_header)
                    original_message_id = inquiry.id  # Assuming your Message model has a message_id field

                    try:
                        email = EmailMessage(
                            subject=subject,
                            body=personalized_message,
                            from_email=from_email,
                            to=[inquiry.from_header],
                        )

                        email.extra_headers = {
                            'In-Reply-To': original_message_id,
                            'References': original_message_id,
                        }

                        email.send()

                        # Save the sent email details to the database
                        SentEmail.objects.create(
                            subject=subject,
                            message=personalized_message,
                            recipient=inquiry.from_header
                        )

                    except Exception as e:
                        self.message_user(request, f"Failed to send email to {inquiry.from_header}. Error: {str(e)}", level='error')
                        return redirect('..')

                self.message_user(request, "Emails successfully sent to selected inquiries.")
                return redirect('..')
        else:
            messages_ids = request.GET.get('ids', '').split(',')
            inquiries = Message.objects.filter(id__in=messages_ids)
            # Get the first inquiry to set initial subject (assuming all inquiries have the same subject)
            initial_subject = inquiries.first().subject if inquiries.exists() else ''
            if initial_subject and not initial_subject.startswith("Re:"):
                initial_subject = "Re: " + initial_subject

            form = EmailReplyForm(initial={'subject': initial_subject})

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



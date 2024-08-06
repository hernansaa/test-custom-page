from django.contrib import admin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import path

from email_client.models import SentEmail

from .models import Inquiry, Enquiry
from .forms import EmailForm

class InquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'nationality', 'phone', 'program', 'created_at']
    list_filter = ['program', 'created_at']
    search_fields = ['name', 'email', 'nationality']
    list_per_page = 20

    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'nationality', 'email', 'phone')
        }),
        ('Program Information', {
            'fields': ('program',)
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )

    readonly_fields = ('created_at',)
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
            form = EmailForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                message_template = form.cleaned_data['message']
                from_email = 'hernan@globalstudies.es'

                inquiry_ids = request.POST.getlist('ids')
                inquiries = Inquiry.objects.filter(id__in=inquiry_ids)

                for inquiry in inquiries:
                    personalized_message = message_template.format(inquiry.name)
                    try:
                        send_mail(subject, personalized_message, from_email, [inquiry.email])

                        # Save the sent email details to the database
                        SentEmail.objects.create(
                            subject=subject,
                            message=personalized_message,
                            recipient=inquiry.email
                        )
                    
                    except Exception as e:
                        self.message_user(request, f"Failed to send email to {inquiry.email}. Error: {str(e)}", level='error')
                        return redirect('..')

                self.message_user(request, "Emails successfully sent to selected inquiries.")
                return redirect('..')
        else:
            form = EmailForm()
            inquiry_ids = request.GET.get('ids', '').split(',')
            inquiries = Inquiry.objects.filter(id__in=inquiry_ids)

        return render(
            request,
            'admin/send_email.html',
            context={'form': form, 'inquiries': inquiries, 'ids': ','.join(inquiry_ids)}
        )
    

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'nationality', 'phone', 'program','branch', 'created_at']
    list_filter = ['program', 'created_at']
    search_fields = ['name', 'email', 'nationality']
    list_per_page = 20

    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'dob', 'nationality', 'email', 'phone')
        }),
        ('Course Information', {
            'fields': ('program', 'course', 'date_start', 'course_weekly_price', 'course_qty_weeks', 'enrollment_fee',
                       )
        }),
        ('Accommodation', {
            'fields': ('accommodation', 'accommodation_qty_weeks')
        }),
        ('Total', {
            'fields': ('total',)
        }),
        ('Assigment', {
            'fields': ('branch',)
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )

    readonly_fields = (
        'name', 'dob', 'nationality', 'email', 'phone',
        'program', 'course', 'date_start', 'course_weekly_price', 'course_qty_weeks', 'enrollment_fee',
        'accommodation', 'accommodation_qty_weeks', 'total', 'created_at',
    )


admin.site.register(Inquiry, InquiryAdmin)
admin.site.register(Enquiry, EnquiryAdmin)

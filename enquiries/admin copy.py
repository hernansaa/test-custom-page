from django.contrib import admin
from django.core.mail import send_mail
from .models import Inquiry
from django.urls import path
from django.shortcuts import render
from .forms import EmailForm


# Register your models here.

class InquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'nationality', 'phone', 'program', 'created_at']
    list_filter = ['program', 'created_at']
    search_fields = ['name', 'email', 'nationality']
    list_per_page = 20  # Number of items to display per page

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
        # Ensure there's at least one inquiry selected
        if queryset.count() == 0:
            self.message_user(request, "No inquiries selected.", level='warning')
            return
        
        subject = 'Your Inquiry'
        message_template = 'Dear {},\n\nThank you for your inquiry regarding our program. We will get back to you shortly.\n\nBest regards,\nThe Admin Team'
        from_email = 'hernan@globalstudies.es'  # Replace with your own email

        for inquiry in queryset:
            personalized_message = message_template.format(inquiry.name)
            try:
                send_mail(subject, personalized_message, from_email, [inquiry.email])
            except Exception as e:
                self.message_user(request, f"Failed to send email to {inquiry.email}. Error: {str(e)}", level='error')
                return

        self.message_user(request, "Emails successfully sent to selected inquiries.")
    
    send_email_action.short_description = "Send email to selected inquiries"

admin.site.register(Inquiry, InquiryAdmin)
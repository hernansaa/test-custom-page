from django.contrib import admin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import path
from django.db import models

from gs_admin.sites import new_admin_site

from django.contrib.admin import register

from unfold.admin import ModelAdmin, TabularInline, StackedInline
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm
from email_client.models import SentEmail

from .models import Inquiry, Enquiry, Contact
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
    


@register(Enquiry, site=new_admin_site)
class EnquiryAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    compressed_fields = True
    list_fullwidth = True
    list_display = ['student', 'rating','follow_up_date', 'email', 'nationality', 'phone', 'program', 'branch', 'employee', 'created_at']
    list_filter = ['rating', 'program', 'branch', 'employee', 'created_at', 'follow_up_date']
    search_fields = ['name', 'surname', 'email', 'nationality']
    list_per_page = 20
    list_editable = ['branch','employee', 'rating', 'follow_up_date',]

    fieldsets = (
        ('Personal Information', {
            'fields': ('name','surname', 'student', 'dob', 'nationality', 'email', 'phone')
        }),
        ('Course Information', {
            'classes': ["wide", "collapse"],
            'fields': ('program', 'course', 'date_start', 'course_weekly_price', 'course_qty_weeks', 'enrollment_fee',
                       )
        }),
        ('Accommodation', {
            'classes': ["wide", "collapse"],
            'fields': ('accommodation', 'accommodation_qty_weeks')
        }),
        ('Total', {
            'classes': ["wide", "collapse"],
            'fields': ('total',)
        }),
        ('Assigment', {
            'classes': ["wide", "collapse"],
            'fields': ('branch', 'employee')
        }),
        ('Follow Up', {
            'classes': ["wide", "collapse"],
            'fields': ('rating', 'follow_up_date',)
        }),
        ('Timestamps', {
            'classes': ["wide", "collapse"],
            'fields': ('created_at',)
        }),
    )

    readonly_fields = (
        'name', 'dob', 'nationality', 'email', 'phone',
        'program', 'course', 'date_start', 'course_weekly_price', 'course_qty_weeks', 'enrollment_fee',
        'accommodation', 'accommodation_qty_weeks', 'total', 'created_at',
    )


class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'nationality', 'email', 'phone', 'branch', 'employee']
    readonly_fields = ['first_name', 'last_name', 'nationality', 'email', 'phone', 'message']
    list_editable = ['branch', 'employee']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    list_filter = ['first_name', 'last_name', 'nationality', 'email', 'phone', 'branch', 'employee']


@register(Contact, site=new_admin_site)
class ContactGsAdmin(ModelAdmin):
    compressed_fields = True # Unfold Admin method
    list_display = ['first_name', 'last_name', 'nationality', 'email', 'phone', 'branch', 'employee']
    readonly_fields = ['first_name', 'last_name', 'nationality', 'email', 'phone', 'message']
    list_editable = ['branch', 'employee']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    list_filter = ['first_name', 'last_name', 'nationality', 'email', 'phone', 'branch', 'employee']


admin.site.register(Inquiry, InquiryAdmin)
admin.site.register(Enquiry, EnquiryAdmin)
admin.site.register(Contact, ContactAdmin)

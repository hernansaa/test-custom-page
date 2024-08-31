from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import register

from gs_admin.sites import new_admin_site

from unfold.admin import ModelAdmin, TabularInline, StackedInline
from unfold.decorators import action, display

from .models import StudentProfile, StudentStatus
from enquiries.models import Enquiry
from quotations.models import Quotation
from invoices.models import Invoice
from enrollments.models import Enrollment

from unfold.contrib.forms.widgets import WysiwygWidget


class EnquiryInline(admin.StackedInline):
    model = Enquiry
    extra = 0  # No extra empty forms by default
    fields = ('view_link', 'rating', 'follow_up_date', 'program', 'course', 'course_qty_weeks', 'date_start', 
              'enrollment_fee','accommodation', 'accommodation_qty_weeks', 'total', 
              'created_at')
    readonly_fields = ('view_link', 'name', 'email', 'phone', 'program', 'course', 'course_qty_weeks',
                       'date_start', 'enrollment_fee', 'created_at', 'total', 'accommodation',
                       'accommodation_qty_weeks')
    ordering = ('-created_at',)
    # tab = True

    def view_link(self, obj):
        url = reverse('admin:enquiries_enquiry_change', args=[obj.pk])
        return format_html('<a href="{}">View Details</a>', url)
    
    view_link.short_description = 'Details'


class EnrollmentInline(admin.StackedInline):
    model = Enrollment
    extra = 0  # No extra empty forms by default
    fields = (
        'id',
        'invoice',
        'student',
        'course',
        'course_qty_weeks',
        'course_date_start',
        'accommodation',
        'accommodation_qty_weeks',
        'accommodation_date_start',
        'airport_transfer',
        'created_at',
        )
    readonly_fields = (
        'id',
        'invoice',
        'student',
        'course',
        'course_qty_weeks',
        'course_date_start',
        'accommodation',
        'accommodation_qty_weeks',
        'accommodation_date_start',
        'airport_transfer',
        'created_at',
        )
    ordering = ('-created_at',)
    # tab = True


class InvoiceInline(admin.StackedInline):
    model = Invoice
    extra = 0  # No extra empty forms by default

    readonly_fields = (
        'enrollment_fee_paid',
        'paid',
        )


class QuotationInline(admin.StackedInline):
    model = Quotation
    extra = 0  # No extra empty forms by default
    fields = (
        'student',
        'school',
        'course',
        'course_qty_weeks',
        'course_date_start',
        'enrollment_fee',
        'course_weekly_price',
        'accommodation',
        'accommodation_qty_weeks',
        'airport_transfer',
        'total',
        'branch',
        'employee'
        )
    readonly_fields = (
        'student',
        'school',
        'course',
        'course_qty_weeks',
        'course_date_start',
        'enrollment_fee',
        'course_weekly_price',
        'accommodation',
        'accommodation_qty_weeks',
        'airport_transfer',
        'total',
        'branch',
        'employee'
        )
    ordering = ('-created_at',)
    # tab = True


class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'email', 'dob', 'branch', 'employee')  
    inlines = [EnquiryInline,
            QuotationInline, 
            InvoiceInline,
            EnrollmentInline,
            ]


admin.site.register(StudentProfile, StudentProfileAdmin)


# UNFOLD ADMIN

class EnquiryInline(StackedInline):
    model = Enquiry
    extra = 0  # No extra empty forms by default
    tab = True
    fields = ('view_link', 'rating', 'follow_up_date', 'program', 'course', 'course_qty_weeks', 'date_start', 
              'enrollment_fee','accommodation', 'accommodation_qty_weeks', 'total', 
              'created_at')
    readonly_fields = ('view_link', 'name', 'email', 'phone', 'program', 'course', 'course_qty_weeks',
                       'date_start', 'enrollment_fee', 'created_at', 'total', 'accommodation',
                       'accommodation_qty_weeks')
    ordering = ('-created_at',)
    # tab = True

    def view_link(self, obj):
        url = reverse('admin:enquiries_enquiry_change', args=[obj.pk])
        return format_html('<a href="{}">View Details</a>', url)
    
    view_link.short_description = 'Details'


class EnrollmentInline(StackedInline):
    model = Enrollment
    extra = 0  # No extra empty forms by default
    tab = True
    fields = (
        'id',
        'invoice',
        'student',
        'course',
        'course_qty_weeks',
        'course_date_start',
        'accommodation',
        'accommodation_qty_weeks',
        'accommodation_date_start',
        'airport_transfer',
        'created_at',
        )
    readonly_fields = (
        'id',
        'invoice',
        'student',
        'course',
        'course_qty_weeks',
        'course_date_start',
        'accommodation',
        'accommodation_qty_weeks',
        'accommodation_date_start',
        'airport_transfer',
        'created_at',
        )
    ordering = ('-created_at',)
    # tab = True


class QuotationInline(StackedInline):
    model = Quotation
    extra = 0  # No extra empty forms by default
    tab = True
    fields = (
        'student',
        'school',
        'course',
        'course_qty_weeks',
        'course_date_start',
        'enrollment_fee',
        'course_weekly_price',
        'accommodation',
        'accommodation_qty_weeks',
        'airport_transfer',
        'total',
        'branch',
        'employee'
        )
    readonly_fields = (
        'student',
        'school',
        'course',
        'course_qty_weeks',
        'course_date_start',
        'enrollment_fee',
        'course_weekly_price',
        'accommodation',
        'accommodation_qty_weeks',
        'airport_transfer',
        'total',
        'branch',
        'employee'
        )
    ordering = ('-created_at',)
    # tab = True


class InvoiceInline(StackedInline):
    model = Invoice
    extra = 0
    tab = True

    readonly_fields = (
        'quotation',
        'invoice_number',
        'city',
        'school',
        'course',
        'course_qty_weeks',
        'course_date_start',
        'school_total',
        'accommodation',
        'accommodation_qty_weeks',
        'accommodation_date_start',
        'accommodation_total',
        'airport_transfer',
        'airport_transfer_total',
        'enrollment_fee',
        'enrollment_fee_paid',
        'total_amount',
        'paid',
        )


@register(StudentProfile, site=new_admin_site)
class StudentProfileAdmin(ModelAdmin):
    compressed_fields = True  
    list_fullwidth = True
    list_display = ('id', 'name', 'surname', 'email', 'dob', 'show_status_customized_color', 'branch', 'employee')
    list_filter = ('name', 'status', 'surname', 'email', 'dob', 'branch', 'employee')
    search_fields = ('id', 'name', 'surname', 'email', 'dob')
    inlines = [
        EnquiryInline, 
        QuotationInline,
        InvoiceInline,
        EnrollmentInline,
        ]
    
    @display(
        description=_("Status"),
        ordering="status",
        label={
            # "success": green, 
            # "warning": orange, 
            # "info": blue, "danger": red
            StudentStatus.ENROLLED: "success",
            StudentStatus.NOT_ENROLLED: "info",
            StudentStatus.STUDYING: "warning",
        },
    )
    def show_status_customized_color(self, obj):
        return obj.status



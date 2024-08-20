from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from django.utils.html import format_html

from gs_admin.sites import new_admin_site

from django.contrib.admin import register

from unfold.admin import ModelAdmin

from .models import StudentProfile
from enquiries.models import Enquiry
from quotations.models import Quotation
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
    tab = True

    def view_link(self, obj):
        url = reverse('admin:enquiries_enquiry_change', args=[obj.pk])
        return format_html('<a href="{}">View Details</a>', url)
    
    view_link.short_description = 'Details'


class EnrollmentInline(admin.StackedInline):
    model = Enrollment
    extra = 0  # No extra empty forms by default
    fields = (
        'student',
        'program',
        'course',
        'course_qty_weeks',
        'date_start',
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
        'program',
        'course',
        'course_qty_weeks',
        'date_start',
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
    tab = True


class QuotationInline(admin.StackedInline):
    model = Quotation
    extra = 0  # No extra empty forms by default
    fields = (
        'student',
        'program',
        'course',
        'course_qty_weeks',
        'date_start',
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
        'program',
        'course',
        'course_qty_weeks',
        'date_start',
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
    tab = True


@register(StudentProfile, site=new_admin_site)
class StudentProfileAdmin(ModelAdmin):
    # Display fields in changeform in compressed mode
    compressed_fields = True  
    
    list_display = ('name', 'surname', 'email', 'dob', 'branch', 'employee')
    list_filter = ('name', 'surname', 'email', 'dob', 'branch', 'employee')
    search_fields = ('name', 'surname', 'email', 'dob')
    inlines = [EnquiryInline, QuotationInline, EnrollmentInline,]


class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'dob', 'branch', 'employee')  
    inlines = [EnquiryInline, QuotationInline, EnrollmentInline,]


admin.site.register(StudentProfile, StudentProfileAdmin)
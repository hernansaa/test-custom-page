from django.contrib import admin
from django.contrib.admin import register
from gs_admin.sites import new_admin_site
from unfold.admin import ModelAdmin
from .models import Quotation

# DJANGO ADMIN CONFIGURATION

class QuotationAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'city',
        'school', 
        'course',
        'course_qty_weeks',
        'total', 
        'status', 
        'course_date_start',
        'created_at'
    )

    list_filter = (
        'school', 
        'course', 
        'status', 
        'created_at'
    )

    search_fields = (
        'student__name', 
        'student__email', 
        'school__name', 
        'course__name'
    )

    readonly_fields = ('created_at',
        'school_total', 
        'accommodation_total', 
        'total', 
        'enrollment_fee', 
        'airport_transfer_total', 
        'enquiry',)

    # list_editable = ('status',)

    fieldsets = (
        ('Student Details', {
            'fields': (
                'student',
                'enquiry', 
            )
        }),
        ('School Location', {
            'fields': (
                'city', 
            )
        }),
        ('School Details', {
            'fields': (
                'school', 
                'course', 
                'course_price_list',
                'course_qty_weeks',
                'course_date_start',
            )
        }),
        ('Accommodation Details', {
            'fields': (
                # 'course_weekly_price', 
                'accommodation',
                'accommodation_price_list',  
                'accommodation_qty_weeks',
                'accommodation_date_start',
            )
        }),
        ('Airport Transfer', {
            'fields': (
                'airport_transfer',
            )
        }),
        ('Quotation Details', {
            'fields': (
                'enrollment_fee',
                'school_total',
                'accommodation_total',
                'airport_transfer_total',
                'total',
            )
        }),
        ('Quatation Status', {
            'fields': (
                'status',
            )
        }),
        ('Other Details', {
            'fields': (
                'branch', 
                'employee', 
            )
        }),
    )

    class Media:
        js = ('js/quotation_admin.js',)
    

admin.site.register(Quotation, QuotationAdmin)




# UNFOLD ADMIN CONFIGURATION


@register(Quotation, site=new_admin_site)
class QuotationAdmin(ModelAdmin):
    # Fields to display in the list view
    list_display = (
        'student',
        'city',
        'school', 
        'course',
        'course_qty_weeks',
        'total', 
        'status', 
        'course_date_start',
        'created_at'
    )

    # Fields to add filters in the list view
    list_filter = (
        'school', 
        'course', 
        'status', 
        'created_at'
    )

    # Fields that can be searched in the list view
    search_fields = (
        'student__name', 
        'student__email', 
        'school__name', 
        'course__name'
    )

    # Editable fields directly from the list view
    # list_editable = ('status',)

    # Fields grouped in the detail view
    fieldsets = (
        ('Student Details', {
            'fields': (
                'student',
                'enquiry', 
            )
        }),
        ('School Location', {
            'fields': (
                'city', 
            )
        }),
        ('School Details', {
            'fields': (
                'school', 
                'course', 
                'course_price_list',
                'course_qty_weeks',
                'course_date_start',
            )
        }),
        ('Accommodation Details', {
            'fields': (
                # 'course_weekly_price', 
                'accommodation',
                'accommodation_price_list',  
                'accommodation_qty_weeks',
                'accommodation_date_start',
            )
        }),
        ('Airport Transfer', {
            'fields': (
                'airport_transfer',
            )
        }),
        ('Quotation Details', {
            'fields': (
                'enrollment_fee',
                'school_total',
                'accommodation_total',
                'airport_transfer_total',
                'total',
            )
        }),
        ('Quatation Status', {
            'fields': (
                'status',
            )
        }),
        ('Other Details', {
            'fields': (
                'branch', 
                'employee', 
            )
        }),
    )

    # Readonly fields (if any)
    readonly_fields = ('created_at',)
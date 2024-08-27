from django.contrib import admin

from gs_admin.sites import new_admin_site

from django.contrib.admin import register

from django.forms import Select

from .models import Quotation

# Register your models here.
class QuotationAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = (
        'student', 
        'school', 
        'course', 
        'date_start', 
        'total', 
        'is_accepted', 
        'created_at'
    )

    # Fields to add filters in the list view
    list_filter = (
        'school', 
        'course', 
        'is_accepted', 
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
    list_editable = ('is_accepted',)

    # Fields grouped in the detail view
    fieldsets = (
        (None, {
            'fields': (
                'student', 
                'enquiry',
                'school', 
                'course', 
                'course_price_list',
                'course_qty_weeks',
                'date_start',
            )
        }),
        ('Accommodation', {
            'fields': (
                # 'course_weekly_price', 
                'accommodation',
                'accommodation_price_list',  
                'accommodation_qty_weeks',
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
                'total',
            )
        }),
        ('Other Details', {
            'fields': (
                'branch', 
                'employee', 
                'is_accepted'
            )
        }),
    )

    # Readonly fields (if any)
    readonly_fields = ('created_at','school_total', 'accommodation_total', 'total', 'enrollment_fee')


    class Media:
        js = ('js/quotation_admin.js',)  # Path to your JS file
    

    # Automatically prepopulate the `total` field (if needed)
    # You may need to implement this in the model or through JS in the admin
    # prepopulated_fields = {'total': ('enrollment_fee', 'course_weekly_price', ...)}
    
    # Automatically save related enrollment if 'is_enrolled' is set to True
    # def save_model(self, request, obj, form, change):
    #     super().save_model(request, obj, form, change)
    #     if obj.is_enrolled:
    #         obj.save()  # This triggers the save logic to create an Enrollment if necessary

# Register the Quotation model with the customized admin interface
admin.site.register(Quotation, QuotationAdmin)





@register(Quotation, site=new_admin_site)
class QuotationAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = (
        'student', 
        'school', 
        'course', 
        'date_start', 
        'total', 
        'is_accepted', 
        'created_at'
    )

    # Fields to add filters in the list view
    list_filter = (
        'school', 
        'course', 
        'is_accepted', 
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
    list_editable = ('is_accepted',)

    # Fields grouped in the detail view
    fieldsets = (
        (None, {
            'fields': (
                'student', 
                'enquiry',
                'school', 
                'course', 
                'course_qty_weeks',
                'date_start',
                'total'
            )
        }),
        ('Fees & Prices', {
            'fields': (
                'enrollment_fee', 
                'course_weekly_price', 
                'accommodation', 
                'accommodation_qty_weeks', 
                'airport_transfer'
            )
        }),
        ('Other Details', {
            'fields': (
                'branch', 
                'employee', 
                'is_accepted'
            )
        }),
    )

    # Readonly fields (if any)
    readonly_fields = ('created_at',)
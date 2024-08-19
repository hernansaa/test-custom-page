from django.contrib import admin

from .models import Quotation

# Register your models here.
class QuotationAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = (
        'student', 
        'program', 
        'course', 
        'date_start', 
        'total', 
        'is_enrolled', 
        'created_at'
    )

    # Fields to add filters in the list view
    list_filter = (
        'program', 
        'course', 
        'is_enrolled', 
        'created_at'
    )

    # Fields that can be searched in the list view
    search_fields = (
        'student__name', 
        'student__email', 
        'program__name', 
        'course__name'
    )

    # Editable fields directly from the list view
    list_editable = ('is_enrolled',)

    # Fields grouped in the detail view
    fieldsets = (
        (None, {
            'fields': (
                'student', 
                'enquiry',
                'program', 
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
                'is_enrolled'
            )
        }),
    )

    # Readonly fields (if any)
    readonly_fields = ('created_at',)

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
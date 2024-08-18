from django.contrib import admin

from gs_admin.sites import new_admin_site

from .models import Quotation

from django.contrib.admin import register

from unfold.admin import ModelAdmin


@register(Quotation, site=new_admin_site)
class QuotationAdmin(ModelAdmin):
    # List display options for the admin list view
    list_display = (
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
        'created_at',
        'branch',
        'employee'
    )

    # Fields to filter by in the admin list view
    list_filter = (
        'program',
        'course',
        'date_start',
        'accommodation',
        'branch',
        'employee',
        'student'
    )

    # Search fields for the admin search bar
    search_fields = (
        'program__name',
        'course__name',
        'accommodation__name',
        'student__name'
    )
    


admin.site.register(Quotation)

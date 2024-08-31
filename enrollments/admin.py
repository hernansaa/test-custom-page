from django.contrib import admin

from gs_admin.sites import new_admin_site

from .models import Enrollment

from django.contrib.admin import register

from unfold.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm


# DJANGO ADMIN

class EnrollmentAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = (
        'id',
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
    
    # Fields to be searchable in the admin interface
    search_fields = (
        'student__name',  # Assuming 'name' is a field in StudentProfile
        'course__name',   # Assuming 'name' is a field in Course
        'city__name',     # Assuming 'name' is a field in City
        'school__name',   # Assuming 'name' is a field in School
    )

    # Filters to be added in the right sidebar of the list view
    list_filter = (
        'city',
        'school',
        'course',
        'accommodation',
        'airport_transfer',
        'created_at',
    )

    # Fields to be used in the detail view
    fields = (
        'id',
        'invoice',
        'student',
        'city',
        'school',
        'course',
        'course_qty_weeks',
        'course_date_start',
        'accommodation',
        'accommodation_qty_weeks',
        'accommodation_date_start',
        'airport_transfer',
    )

    readonly_fields = (
        'id',
        'invoice',
        'student',
        'city',
        'school',
        'course',
        'course_qty_weeks',
        'course_date_start',
        'accommodation',
        'accommodation_qty_weeks',
        'accommodation_date_start',
        'airport_transfer',
    )

    # Optionally, you can specify which fields to include in the form view for adding/editing
    # and customize how they are laid out.
    # You can also use `fieldsets` to group fields into sections.

    # Set ordering of the records in the list view
    ordering = ('-created_at',)

    # List how many records should be shown per page
    list_per_page = 25


# Register the Enrollment model with the Django admin site
admin.site.register(Enrollment, EnrollmentAdmin)




# UNFOLD ADMIN


@register(Enrollment, site=new_admin_site)
class EnrollmentAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    compressed_fields = True
    list_fullwidth = True
    list_display = (
        'id',
        'student',
        'course',
        'course_qty_weeks',
        'course_date_start',
        'course_date_finish',
        'accommodation',
        'accommodation_qty_weeks',
        'accommodation_date_start',
        'accommodation_date_finish',
        'airport_transfer',
        'created_at',
    )
    
    # Fields to be searchable in the admin interface
    search_fields = (
        'student__name',  # Assuming 'name' is a field in StudentProfile
        'course__name',   # Assuming 'name' is a field in Course
        'city__name',     # Assuming 'name' is a field in City
        'school__name',   # Assuming 'name' is a field in School
    )

    # Filters to be added in the right sidebar of the list view
    list_filter = (
        'city',
        'school',
        'course',
        'accommodation',
        'airport_transfer',
        'course_date_start',
        'created_at',
    )

    # Fields to be used in the detail view
    fields = (
        'id',
        'invoice',
        'student',
        'city',
        'school',
        'course',
        'course_qty_weeks',
        'course_date_start',
        'course_date_finish',
        'accommodation',
        'accommodation_qty_weeks',
        'accommodation_date_start',
        'accommodation_date_finish',
        'airport_transfer',
    )

    readonly_fields = (
        'id',
        'invoice',
        'student',
        'city',
        'school',
        'course',
        'course_qty_weeks',
        'course_date_start',
        'course_date_finish',
        'accommodation',
        'accommodation_qty_weeks',
        'accommodation_date_start',
        'accommodation_date_finish',
        'airport_transfer',
    )

    # Optionally, you can specify which fields to include in the form view for adding/editing
    # and customize how they are laid out.
    # You can also use `fieldsets` to group fields into sections.

    # Set ordering of the records in the list view
    ordering = ('-created_at',)

    # List how many records should be shown per page
    list_per_page = 25



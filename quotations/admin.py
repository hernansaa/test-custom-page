from django.contrib import admin
from smart_selects.db_fields import ChainedForeignKey
from django.contrib.admin import register
from django.urls import path
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

from gs_admin.sites import new_admin_site

from unfold.admin import ModelAdmin
from unfold.decorators import action, display
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm

from .forms import QuotationAdminForm

from .models import Quotation, QuotationStatus


# DJANGO ADMIN CONFIGURATION


class QuotationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student',
        'city',
        'school', 
        'course',
        'course_qty_weeks',
        'total', 
        'status', 
        'course_date_start',
        'course_date_finish',
        'created_at',
        'send_email_button'
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
            "classes": ["wide", "collapse"],
            'fields': (
                'city', 
            )
        }),
        ('School Details', {
            "classes": ["wide", "collapse"],
            'fields': (
                'school', 
                'course', 
                'course_price_list',
                'course_qty_weeks',
                'course_date_start',
                'course_date_finish',
            )
        }),
        ('Accommodation Details', {
            "classes": ["wide", "collapse"],
            'fields': (
                # 'course_weekly_price', 
                'accommodation',
                'accommodation_price_list',  
                'accommodation_qty_weeks',
                'accommodation_date_start',
                'accommodation_date_finish',
            )
        }),
        ('Airport Transfer', {
            "classes": ["wide", "collapse"],
            'fields': (
                'airport_transfer',
            )
        }),
        ('Quotation Details', {
            "classes": ["wide", "collapse"],
            'fields': (
                'enrollment_fee',
                'school_total',
                'accommodation_total',
                'airport_transfer_total',
                'total',
            )
        }),
        ('Quatation Status', {
            "classes": ["wide", "collapse"],
            'fields': (
                'status',
            )
        }),
        ('Other Details', {
            "classes": ["wide", "collapse"],
            'fields': (
                'branch', 
                'employee', 
            )
        }),
    )


    def send_email_button(self, obj):
        return f'<a class="button" href="/admin/app_name/order/{obj.id}/send_email/">Send Email</a>'  
    send_email_button.short_description = 'Send Email'
    send_email_button.allow_tags = True


    class Media:
        js = ('js/quotation_admin.js',)
    

admin.site.register(Quotation, QuotationAdmin)




# UNFOLD ADMIN CONFIGURATION


@register(Quotation, site=new_admin_site)
class QuotationAdmin(admin.ModelAdmin):
    form = QuotationAdminForm
    import_form_class = ImportForm
    export_form_class = ExportForm
    list_fullwidth = True
    list_display = (
        'id',
        'student',
        'city',
        'school', 
        'course',
        'course_qty_weeks',
        'accommodation',
        'accommodation_qty_weeks',
        'total', 
        "show_status_customized_color", 
        'course_date_start',
        'course_date_finish',
        'accommodation_date_start',
        'accommodation_date_finish',
        'created_at',
        'send_email_button',
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

    # Editable fields directly from the list view
    # list_editable = ('status',)

    readonly_fields = ('created_at',
        'school_total', 
        'accommodation_total', 
        'total', 
        'enrollment_fee', 
        'airport_transfer_total', 
        'enquiry',
        'send_email_button',
        )

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
            # "classes": ["wide", "collapse"],
            'fields': (
                'school', 
                'course', 
                'course_price_list',
                'course_qty_weeks',
                'course_date_start',
                'course_date_finish',
            )
        }),
        ('Accommodation Details', {
            'fields': (
                # 'course_weekly_price', 
                'accommodation',
                'accommodation_price_list',  
                'accommodation_qty_weeks',
                'accommodation_date_start',
                'accommodation_date_finish',
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
        ('Send E-mail', {
            'fields': (
                'send_email_button',
            )
        }),
        ('Other Details', {
            'fields': (
                'branch', 
                'employee', 
            )
        }),
    )

    # autocomplete_fields = ['student']

    # def get_form(self, request, obj=None, change=False, **kwargs):
    #     form = super().get_form(request, obj, change, **kwargs)
    #     form.base_fields["status"].widget = UnfoldAdminColorInputWidget()
    #     return form


    @display(
        description=_("Status"),
        ordering="status",
        label={
            QuotationStatus.APPROVED: "success",
            QuotationStatus.PENDING: "warning",
            QuotationStatus.REJECTED: "danger",
        },
    )
    def show_status_customized_color(self, obj):
        return obj.status
    
    def send_email_button(self, obj):
        return mark_safe(f'<a class="button" href="/admin/app_name/order/{obj.id}/send_email/">Send Email</a>')
    
    send_email_button.short_description = 'Send Email'
    send_email_button.allow_tags = True

    # def get_urls(self):
    #     urls = super().get_urls()
    #     custom_urls = [
    #         path(
    #             '<int:order_id>/send_email/',
    #             self.admin_site.admin_view(self.send_email),
    #             name='send-email',
    #         ),
    #     ]
    #     return custom_urls + urls


    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        obj = self.get_object(request, object_id)
        form = self.get_form(request, obj)(request.POST or None, instance=obj)
        extra_context['form'] = form
        extra_context['quotation'] = Quotation.objects.get(id=object_id)
        return super().change_view(request, object_id, form_url, extra_context=extra_context)


    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        form = self.get_form(request)(request.POST or None)
        extra_context['form'] = form
        return super().add_view(request, form_url, extra_context=extra_context)
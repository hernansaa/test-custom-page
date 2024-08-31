from django.contrib import admin
from django.contrib.admin import register
from django.utils.translation import gettext_lazy as _

from import_export.admin import ImportExportModelAdmin

from unfold.admin import ModelAdmin
from unfold.decorators import action, display
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm

from gs_admin.sites import new_admin_site


from .models import Transaction, TransactionType


# DJANGO ADMIN

@register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'type',
        'invoice', 
        'amount', 
        'currency', 
        'payment_method', 
        'status', 
        'transaction_date', 
        'transaction_fee',
    )
    list_filter = (
        'payment_method', 
        'status', 
        'currency', 
        'transaction_date',
    )
    search_fields = (
        'id', 
        'invoice__id', 
        'description', 
        'reference',
    )
    ordering = ['-transaction_date']
    readonly_fields = ['transaction_date']  
    fieldsets = (
        (None, {
            'fields': (
                'type', 
                'invoice', 
                'amount', 
                'currency', 
                'payment_method', 
                'status', 
                'transaction_fee'
            ),
        }),
        ('Additional Information', {
            'fields': (
                'reference', 
                'description', 
                'receipt', 
                'related_transactions'
            ),
            'classes': (
                'collapse',
            ),
        }),
        ('Date Information', {
            'fields': (
                'transaction_date',
            ),
        }),
    )
    filter_horizontal = ('related_transactions',)  # Use filter widget for related transactions
    autocomplete_fields = ['invoice']  # Enable autocomplete for Invoice if many records


# UNFOLD ADMIN


@register(Transaction, site=new_admin_site)
class TransactionAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    list_fullwidth = True
    list_display = (
        'id',
        'show_type_customized_color',
        'invoice', 
        'amount', 
        'currency', 
        'payment_method', 
        'status', 
        'transaction_date', 
        'transaction_fee',
        'receipt',
    )
    list_filter = (
        'payment_method', 
        'status', 
        'type',
        'currency', 
        'transaction_date',
    )
    search_fields = (
        'id', 
        'invoice__id',  
        'description', 
        'reference',
    )
    ordering = ['-transaction_date']
    readonly_fields = ['transaction_date']  
    fieldsets = (
        ('Invoice details', {
            'fields': (
            'type', 
            'invoice', 
            'amount', 
            'currency', 
            'payment_method', 
            'status', 
            'transaction_fee'
            )
        }),
        ('Additional Information', {
            'fields': (
                'reference', 
                'description', 
                'receipt', 
                'related_transactions',
            ),
            'classes': (
                'collapse',
            ),
        }),
        ('Date Information', {
            'fields': (
                'transaction_date',
            ),
        }),
    )
    filter_horizontal = ('related_transactions',)  # Use filter widget for related transactions
    autocomplete_fields = ['invoice']  # Enable autocomplete for Invoice if many records

    @display(
        description=_("Type"),
        ordering="type",
        label={
            TransactionType.IN: "success",  # green / "warning" orange
            TransactionType.OUT: "danger",
        },
    )
    def show_type_customized_color(self, obj):
        return obj.type
from django.contrib import admin
from django.contrib.admin import register

from gs_admin.sites import new_admin_site

from unfold.admin import ModelAdmin

from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm

from .models import Transaction


# DJANGO ADMIN

class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
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
        'invoice__id',  # Assuming Invoice has an ID field
        'description', 
        'reference',
    )
    ordering = ['-transaction_date']
    readonly_fields = ['transaction_date']  # Make the transaction date read-only
    fieldsets = (
        (None, {
            'fields': ('invoice', 'amount', 'currency', 'payment_method', 'status', 'transaction_fee')
        }),
        ('Additional Information', {
            'fields': ('reference', 'description', 'receipt', 'related_transactions'),
            'classes': ('collapse',),
        }),
        ('Date Information', {
            'fields': ('transaction_date',),
        }),
    )
    filter_horizontal = ('related_transactions',)  # Use filter widget for related transactions
    autocomplete_fields = ['invoice']  # Enable autocomplete for Invoice if many records

admin.site.register(Transaction, TransactionAdmin)



# UNFOLD ADMIN

@register(Transaction, site=new_admin_site)
class TransactionAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    list_fullwidth = True
    list_display = (
        'id', 
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
        'currency', 
        'transaction_date',
    )
    search_fields = (
        'id', 
        'invoice__id',  # Assuming Invoice has an ID field
        'description', 
        'reference',
    )
    ordering = ['-transaction_date']
    readonly_fields = ['transaction_date']  # Make the transaction date read-only
    fieldsets = (
        ('Invoice details', {
            'fields': ('invoice', 'amount', 'currency', 'payment_method', 'status', 'transaction_fee')
        }),
        ('Additional Information', {
            'fields': ('reference', 'description', 'receipt', 'related_transactions'),
            'classes': ('collapse',),
        }),
        ('Date Information', {
            'fields': ('transaction_date',),
        }),
    )
    filter_horizontal = ('related_transactions',)  # Use filter widget for related transactions
    autocomplete_fields = ['invoice']  # Enable autocomplete for Invoice if many records
from django.contrib import admin

from .models import Invoice, Payment


class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0


class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        'invoice_number',
        'get_student_name',
        'quotation',
        'date_issued', 
        'enrollment_fee',
        'enrollment_fee_paid', 
        'total_amount',
        'total_paid',
        'outstanding_balance',
        'paid',
        'school',
        'course',
        'course_qty_weeks',
        'school_total',
        'accommodation',
        'accommodation_qty_weeks',
        'accommodation_total',
        'airport_transfer',
        'airport_transfer_total',
        'created_at',
        )
    
    search_fields = (
        'invoice_number', 
        'quotation__student__name',
        )
    
    list_filter = (
        'paid', 
        'date_issued'
        )
    
    readonly_fields = (
        'quotation',
        'invoice_number', 
        'date_issued', 
        'enrollment_fee',
        'enrollment_fee_paid', 
        'total_amount',
        'total_paid',
        'outstanding_balance',
        'paid',
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
        'created_at',
        )
    
    ordering = ('-date_issued',)
    
    fieldsets = (
        ('INVOICE DETAILS', {
            'fields': (
                'invoice_number', 
                'quotation', 
                'date_issued',
                'created_at',
                'enrollment_fee_paid',
                'total_amount',
                'total_paid',
                'outstanding_balance',
                'paid',
            )
        }),
        ('PROGRAM DETAILS', {
            'fields': (
                'enrollment_fee',
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
            )
        }),
        )
    

    inlines = [PaymentInline]

    # Optional: Custom actions (e.g., mark invoices as paid)
    actions = ['mark_as_paid']

    def get_student_name(self, obj):
        """Returns the student's name from the related Quotation."""
        return obj.quotation.student.name + ' ' + obj.quotation.student.surname if obj.quotation and obj.quotation.student else None
    get_student_name.short_description = 'Student'
    
    # def mark_as_paid(self, request, queryset):
    #     """Custom admin action to mark selected invoices as paid."""
    #     updated = queryset.update(paid=True)
    #     self.message_user(request, f"{updated} invoices successfully marked as paid.")
    # mark_as_paid.short_description = "Mark selected invoices as paid"


admin.site.register(Invoice, InvoiceAdmin)





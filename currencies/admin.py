from django.contrib import admin
from .models import Currency

# Register your models here.

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'symbol']
    list_filter = ['code', 'name', 'symbol']
    search_fields = ['code', 'name', 'symbol']
    list_per_page = 20



admin.site.register(Currency, CurrencyAdmin)

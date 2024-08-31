from django.contrib import admin
from django.contrib.admin import register

from unfold.admin import ModelAdmin
from gs_admin.sites import new_admin_site

from .models import Currency



# DJANGO ADMIN


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'symbol']
    list_filter = ['code', 'name', 'symbol']
    search_fields = ['code', 'name', 'symbol']
    list_per_page = 20


admin.site.register(Currency, CurrencyAdmin)



# UNFOLD ADMIN

@register(Currency, site=new_admin_site)
class CurrencyAdmin(ModelAdmin):
    list_display = ['code', 'name', 'symbol']
    list_filter = ['code', 'name', 'symbol']
    search_fields = ['code', 'name', 'symbol']
    list_per_page = 20


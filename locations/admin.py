from django.contrib import admin
from .models import Country, State, City

# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country__name')
    list_filter = ('country',)
    ordering = ('name',)

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'country')
    search_fields = ('name', 'state__name', 'state__country__name')
    list_filter = ('state', 'state__country')
    ordering = ('name',)

    def country(self, obj):
        return obj.state.country.name
    country.admin_order_field = 'state__country'  # Allows column to be sorted
    country.short_description = 'Country'         # Renames column head

admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)

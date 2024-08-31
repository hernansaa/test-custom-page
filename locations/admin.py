from django.contrib import admin
from django.contrib.admin import register

from unfold.admin import ModelAdmin
from gs_admin.sites import new_admin_site

from .models import Country, State, City

# DJANGO ADMIN


@register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country__name')
    list_filter = ('country',)
    ordering = ('name',)


@register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'country')
    search_fields = ('name', 'state__name', 'state__country__name')
    list_filter = ('state', 'state__country')
    ordering = ('name',)

    def country(self, obj):
        return obj.state.country.name
    country.admin_order_field = 'state__country'  # Allows column to be sorted
    country.short_description = 'Country'         # Renames column head



# UNFOLD ADMIN


@register(Country, site=new_admin_site)
class CountryAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@register(State, site=new_admin_site)
class StateAdmin(ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country__name')
    list_filter = ('country',)
    ordering = ('name',)

@register(City, site=new_admin_site)
class CityAdmin(ModelAdmin):
    list_display = ('name', 'state', 'country')
    search_fields = ('name', 'state__name', 'state__country__name')
    list_filter = ('state', 'state__country')
    ordering = ('name',)

    def country(self, obj):
        return obj.state.country.name
    country.admin_order_field = 'state__country'  # Allows column to be sorted
    country.short_description = 'Country'         # Renames column head
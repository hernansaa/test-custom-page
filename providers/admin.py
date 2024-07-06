from django.contrib import admin

from .models import (
    School,
    Facility, 
    SchoolFacility, 
    Language, 
    SchoolContactInformation, 
    Address, 
    Acreditation, 
    SchoolAcreditation,
    Activity,
    SchoolActivity,
    Accommodation,
    SchoolAccommodation
)

# Register your models here.


class FacilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon')


class SchoolFacilityInline(admin.TabularInline):
    model = SchoolFacility
    extra = 1


class AcreditationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo')


class SchoolAcreditationInline(admin.TabularInline):
    model = SchoolAcreditation
    extra = 1


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'img')


class SchoolActivityInline(admin.TabularInline):
    model = SchoolActivity
    extra = 1


class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'description', 'img')


class SchoolAccommodationInline(admin.TabularInline):
    model = SchoolAccommodation
    extra = 1


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    inlines = [SchoolFacilityInline, SchoolAcreditationInline, SchoolActivityInline, SchoolAccommodationInline]


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class SchoolContactInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')



admin.site.register(School, SchoolAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Acreditation, AcreditationAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Accommodation, AccommodationAdmin)
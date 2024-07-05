from django.contrib import admin

from .models import School, Facility, SchoolFacility, Language, SchoolContactInformation, Address, Acreditation, SchoolAcreditation

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


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    inlines = [SchoolFacilityInline, SchoolAcreditationInline]


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class SchoolContactInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')



admin.site.register(School, SchoolAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Acreditation, AcreditationAdmin)
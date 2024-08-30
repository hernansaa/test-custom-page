from django.contrib import admin
from django.db import models 
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import register

from branches.models import AgencyBranch

from gs_admin.sites import new_admin_site

from unfold.admin import ModelAdmin, TabularInline, StackedInline

from .models import (
    School,
    Facility, 
    SchoolFacility, 
    Language, 
    ContactInformation, 
    Address, 
    Acreditation, 
    SchoolAcreditation,
    Activity,
    SchoolActivity,
    Accommodation,
    SchoolAccommodation,
    Airport,
    SchoolAirportTransfer,
    Extra,
    SchoolExtra,
    AvgAge,
    SchoolAvgAge,
    ClassroomEquipment,
    SchoolClassroomEquipment,
    NationalityMix,
    SchoolAgencyBranch,
    Course,
    Address,
    #CoursePrice,
    AccommodationPrice,
    AccommodationPriceList,
    CoursePrice,
    CoursePriceList,
)


# UNFOLD ADMIN


class SchoolFacilityInline(TabularInline):
    model = SchoolFacility
    extra = 0


class SchoolAcreditationInline(TabularInline):
    model = SchoolAcreditation
    extra = 0


class SchoolActivityInline(TabularInline):
    model = SchoolActivity
    extra = 0


class SchoolAccommodationInline(TabularInline):
    model = SchoolAccommodation
    extra = 0


class SchoolAirportTransferInline(TabularInline):
    model = SchoolAirportTransfer
    extra = 0


class SchoolExtraline(TabularInline):
    model = SchoolExtra
    extra = 0


class SchoolAvgAgeline(TabularInline):
    model = SchoolAvgAge
    extra = 0


class SchoolClassroomEquipmentline(TabularInline):
    model = SchoolClassroomEquipment
    extra = 0


class SchoolNationalityMixline(TabularInline):
    model = NationalityMix
    extra = 0


class ContactInformationInline(TabularInline):
    model = ContactInformation
    extra = 0


class SchoolAgencyBranchInline(TabularInline):
    model = SchoolAgencyBranch
    extra = 0


class CourseInline(StackedInline):
    model = Course
    extra = 0
    tab = True


class AddressInline(TabularInline):
    model = Address
    extra = 0


@register(School, site=new_admin_site)
class SchoolAdmin(ModelAdmin):
    compressed_fields = True  # Unfold Admin method
    list_display = ('name', 'language_id')
    search_fields = ('name', 'language_id__name')
    list_filter = ('name', 'language_id__name')
    list_fullwidth = True
    inlines = [
        SchoolFacilityInline,
        SchoolAcreditationInline, 
        SchoolActivityInline, 
        SchoolAccommodationInline,
        SchoolAirportTransferInline,
        SchoolExtraline,
        SchoolAvgAgeline,
        SchoolClassroomEquipmentline,
        SchoolNationalityMixline,
        ContactInformationInline,
        SchoolAgencyBranchInline,
        CourseInline,
        AddressInline,
    ]

    # def change_view(self, request, object_id, form_url='', extra_context=None):
    #     extra_context = extra_context or {}

    #     # Use the form specified in the admin class
    #     form_class = self.get_form(request, obj=None)
    #     form = form_class(request.POST or None, instance=self.get_object(request, object_id))

    #     extra_context['form'] = form

    #     return super().change_view(request, object_id, form_url, extra_context=extra_context)


# DJANGO ADMIN

class SchoolFacilityInline(admin.TabularInline):
    model = SchoolFacility
    extra = 1


class SchoolAcreditationInline(admin.TabularInline):
    model = SchoolAcreditation
    extra = 1


class SchoolActivityInline(admin.TabularInline):
    model = SchoolActivity
    extra = 1


class SchoolAccommodationInline(admin.TabularInline):
    model = SchoolAccommodation
    extra = 1


class SchoolAirportTransferInline(admin.TabularInline):
    model = SchoolAirportTransfer
    extra = 1

class SchoolExtraline(admin.TabularInline):
    model = SchoolExtra
    extra = 1


class SchoolAvgAgeline(admin.TabularInline):
    model = SchoolAvgAge
    extra = 1


class SchoolClassroomEquipmentline(admin.TabularInline):
    model = SchoolClassroomEquipment
    extra = 1


class SchoolNationalityMixline(admin.TabularInline):
    model = NationalityMix
    extra = 1


class ContactInformationInline(admin.TabularInline):
    model = ContactInformation
    extra = 1


class SchoolAgencyBranchInline(admin.TabularInline):
    model = SchoolAgencyBranch
    extra = 1


class CourseInline(admin.StackedInline):
    model = Course
    extra = 1


class AddressInline(admin.TabularInline):
    model = Address
    extra = 1


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'language_id')
    search_fields = ('name', 'language_id__name')
    list_filter = ('name', 'language_id__name')
    save_as = True
    inlines = [
        SchoolFacilityInline,
        SchoolAcreditationInline, 
        SchoolActivityInline, 
        SchoolAccommodationInline,
        SchoolAirportTransferInline,
        SchoolExtraline,
        SchoolAvgAgeline,
        SchoolClassroomEquipmentline,
        SchoolNationalityMixline,
        ContactInformationInline, 
        SchoolAgencyBranchInline,
        CourseInline,
        AddressInline,
    ]



class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'description', 'img')


class AirportAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city')


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'img')


class ExtraAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class FacilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon')


class AvgAgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_age', 'to_age')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'street', 'school')


class ClassroomEquipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon')


class AcreditationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo')


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class SchoolContactInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class CoursePriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'qty_weeks')


class CoursePriceInline(admin.TabularInline):
    model = CoursePrice
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'school')
    # inlines = [
    #     CoursePriceInline,
    # ]


class AccommodationPriceInline(admin.TabularInline):
    model = AccommodationPrice
    extra = 1


class AccommodationPriceListAdmin(admin.ModelAdmin):
    list_display = ('school_accommodation', 'year')
    inlines = [
        AccommodationPriceInline,
    ]


class CoursePriceListAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'year')
    inlines = [
        CoursePriceInline,
    ]



admin.site.register(School, SchoolAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Acreditation, AcreditationAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Accommodation, AccommodationAdmin)
admin.site.register(Airport, AirportAdmin)
admin.site.register(Extra, ExtraAdmin)
admin.site.register(AvgAge, AvgAgeAdmin)
admin.site.register(ClassroomEquipment, ClassroomEquipmentAdmin)
admin.site.register(NationalityMix)
admin.site.register(ContactInformation)
admin.site.register(Course, CourseAdmin)
admin.site.register(Address, AddressAdmin)
# admin.site.register(CoursePrice) Not needed so far since I have it as inline in the CoursePriceList Admin
admin.site.register(CoursePriceList, CoursePriceListAdmin)
# admin.site.register(AccommodationPrice) # Not needed so far since I have it as inline in the AccommodationPriceList Admin
admin.site.register(AccommodationPriceList, AccommodationPriceListAdmin)
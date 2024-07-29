from django.contrib import admin

from branches.models import AgencyBranch

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


class AirportAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city')


class SchoolAirportTransferInline(admin.TabularInline):
    model = SchoolAirportTransfer
    extra = 1


class ExtraAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class SchoolExtraline(admin.TabularInline):
    model = SchoolExtra
    extra = 1


class AvgAgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_age', 'to_age')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'school')


class SchoolAvgAgeline(admin.TabularInline):
    model = SchoolAvgAge
    extra = 1


class ClassroomEquipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon')


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


class CourseInline(admin.TabularInline):
    model = Course
    extra = 1


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
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
    ]


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
admin.site.register(Airport, AirportAdmin)
admin.site.register(Extra, ExtraAdmin)
admin.site.register(AvgAge, AvgAgeAdmin)
admin.site.register(ClassroomEquipment, ClassroomEquipmentAdmin)
admin.site.register(NationalityMix)
admin.site.register(ContactInformation)
admin.site.register(Course, CourseAdmin)
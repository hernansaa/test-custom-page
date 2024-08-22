from django.contrib import admin
from django.db import models

from django.utils.translation import gettext_lazy as _

from branches.models import AgencyBranch

from gs_admin.sites import new_admin_site

from django.contrib.admin import register

from unfold.admin import ModelAdmin
from unfold.widgets import (UnfoldAdminSplitDateTimeWidget, UnfoldAdminSplitDateTimeVerticalWidget, 
                            UnfoldAdminDateWidget, AdminDateWidget, UnfoldAdminSingleDateWidget,
                            UnfoldAdminTextareaWidget, UnfoldAdminSelectWidget, UnfoldAdminIntegerFieldWidget,
                            UnfoldAdminTextInputWidget)
from unfold.contrib.forms.widgets import ArrayWidget, WysiwygWidget


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

# Register your models here.


class FacilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon')


class SchoolFacilityInline(admin.TabularInline):
    model = SchoolFacility
    extra = 1

    formfield_overrides = {
        models.TextField: {
            "widget": UnfoldAdminTextareaWidget,
        },
        models.CharField: {
            "widget": UnfoldAdminTextInputWidget,
        },
        models.TextChoices: {
            "widget": UnfoldAdminSelectWidget,
        },
        models.IntegerField: {
            "widget": UnfoldAdminIntegerFieldWidget,
        },
        models.Choices: {
            "widget": UnfoldAdminSelectWidget,
        },
    }


class AcreditationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo')


class SchoolAcreditationInline(admin.TabularInline):
    model = SchoolAcreditation
    extra = 1

    formfield_overrides = {
        models.TextField: {
            "widget": UnfoldAdminTextareaWidget,
        },
        models.CharField: {
            "widget": UnfoldAdminTextInputWidget,
        },
        models.TextChoices: {
            "widget": UnfoldAdminSelectWidget,
        },
        models.IntegerField: {
            "widget": UnfoldAdminIntegerFieldWidget,
        },
        models.Choices: {
            "widget": UnfoldAdminSelectWidget,
        },
    }



class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'img')


class SchoolActivityInline(admin.TabularInline):
    model = SchoolActivity
    extra = 1

    formfield_overrides = {
        models.TextField: {
            "widget": UnfoldAdminTextareaWidget,
        },
        models.CharField: {
            "widget": UnfoldAdminTextInputWidget,
        },
        models.TextChoices: {
            "widget": UnfoldAdminSelectWidget,
        },
        models.IntegerField: {
            "widget": UnfoldAdminIntegerFieldWidget,
        },
        models.Choices: {
            "widget": UnfoldAdminSelectWidget,
        },
    }


class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'description', 'img')


class SchoolAccommodationInline(admin.TabularInline):
    model = SchoolAccommodation
    extra = 1
    tab = True

    formfield_overrides = {
        models.TextField: {
            "widget": UnfoldAdminTextareaWidget,
        },
        models.CharField: {
            "widget": UnfoldAdminTextInputWidget,
        },
        models.TextChoices: {
            "widget": UnfoldAdminSelectWidget,
        },
        models.IntegerField: {
            "widget": UnfoldAdminIntegerFieldWidget,
        },
        models.Choices: {
            "widget": UnfoldAdminSelectWidget,
        },
    }


class AirportAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city')


class SchoolAirportTransferInline(admin.TabularInline):
    model = SchoolAirportTransfer
    extra = 1

    formfield_overrides = {
        models.TextField: {
            "widget": UnfoldAdminTextareaWidget,
        },
        models.CharField: {
            "widget": UnfoldAdminTextInputWidget,
        },
        models.TextChoices: {
            "widget": UnfoldAdminSelectWidget,
        },
        models.IntegerField: {
            "widget": UnfoldAdminIntegerFieldWidget,
        },
        models.Choices: {
            "widget": UnfoldAdminSelectWidget,
        },
    }


class ExtraAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class SchoolExtraline(admin.TabularInline):
    model = SchoolExtra
    extra = 1

    formfield_overrides = {
        models.TextField: {
            "widget": UnfoldAdminTextareaWidget,
        },
        models.CharField: {
            "widget": UnfoldAdminTextInputWidget,
        },
        models.TextChoices: {
            "widget": UnfoldAdminSelectWidget,
        },
        models.IntegerField: {
            "widget": UnfoldAdminIntegerFieldWidget,
        },
        models.Choices: {
            "widget": UnfoldAdminSelectWidget,
        },
    }


class AvgAgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_age', 'to_age')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'street', 'school')


class SchoolAvgAgeline(admin.TabularInline):
    model = SchoolAvgAge
    extra = 1

    formfield_overrides = {
        models.TextField: {
            "widget": UnfoldAdminTextareaWidget,
        },
        models.CharField: {
            "widget": UnfoldAdminTextInputWidget,
        },
        models.TextChoices: {
            "widget": UnfoldAdminSelectWidget,
        },
        models.IntegerField: {
            "widget": UnfoldAdminIntegerFieldWidget,
        },
        models.Choices: {
            "widget": UnfoldAdminSelectWidget,
        },
    }


class ClassroomEquipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon')


class SchoolClassroomEquipmentline(admin.TabularInline):
    model = SchoolClassroomEquipment
    extra = 1

    formfield_overrides = {
        models.TextField: {
            "widget": UnfoldAdminTextareaWidget,
        },
        models.CharField: {
            "widget": UnfoldAdminTextInputWidget,
        },
        models.TextChoices: {
            "widget": UnfoldAdminSelectWidget,
        },
        models.IntegerField: {
            "widget": UnfoldAdminIntegerFieldWidget,
        },
        models.Choices: {
            "widget": UnfoldAdminSelectWidget,
        },
    }


class SchoolNationalityMixline(admin.TabularInline):
    model = NationalityMix
    extra = 1

    formfield_overrides = {
        models.TextField: {
            "widget": UnfoldAdminTextareaWidget,
        },
        models.CharField: {
            "widget": UnfoldAdminTextInputWidget,
        },
        models.TextChoices: {
            "widget": UnfoldAdminSelectWidget,
        },
        models.IntegerField: {
            "widget": UnfoldAdminIntegerFieldWidget,
        },
        models.Choices: {
            "widget": UnfoldAdminSelectWidget,
        },
    }


class ContactInformationInline(admin.TabularInline):
    model = ContactInformation
    extra = 1

    formfield_overrides = {
        models.TextField: {
            "widget": UnfoldAdminTextareaWidget,
        },
        models.CharField: {
            "widget": UnfoldAdminTextInputWidget,
        },
        models.TextChoices: {
            "widget": UnfoldAdminSelectWidget,
        },
        models.IntegerField: {
            "widget": UnfoldAdminIntegerFieldWidget,
        },
        models.Choices: {
            "widget": UnfoldAdminSelectWidget,
        },
    }


class SchoolAgencyBranchInline(admin.TabularInline):
    model = SchoolAgencyBranch
    extra = 1

    formfield_overrides = {
        models.TextField: {
            "widget": UnfoldAdminTextareaWidget,
        },
        models.CharField: {
            "widget": UnfoldAdminTextInputWidget,
        },
        models.TextChoices: {
            "widget": UnfoldAdminSelectWidget,
        },
        models.IntegerField: {
            "widget": UnfoldAdminIntegerFieldWidget,
        },
        models.Choices: {
            "widget": UnfoldAdminSelectWidget,
        },
    }


class CourseInline(admin.StackedInline):
    model = Course
    extra = 1
    # tab = True
    # hide_title = True

    formfield_overrides = {
        models.TextField: {
            "widget": UnfoldAdminTextareaWidget,
        },
        models.CharField: {
            "widget": UnfoldAdminTextInputWidget,
        },
        models.TextChoices: {
            "widget": UnfoldAdminSelectWidget,
        },
        models.IntegerField: {
            "widget": UnfoldAdminIntegerFieldWidget,
        },
        models.Choices: {
            "widget": UnfoldAdminSelectWidget,
        },
    }


class AddressInline(admin.TabularInline):
    model = Address
    extra = 1

    formfield_overrides = {
        models.TextField: {
            "widget": UnfoldAdminTextareaWidget,
        },
        models.CharField: {
            "widget": UnfoldAdminTextInputWidget,
        },
        models.TextChoices: {
            "widget": UnfoldAdminSelectWidget,
        },
        models.IntegerField: {
            "widget": UnfoldAdminIntegerFieldWidget,
        },
        models.Choices: {
            "widget": UnfoldAdminSelectWidget,
        },
    }


@register(School, site=new_admin_site)
class SchoolAdmin(ModelAdmin):
    compressed_fields = True # Unfold Admin method
    
    list_display = ('name', 'language_id')
    search_fields = ('name', 'language_id__name')
    list_filter = ('name', 'language_id__name')
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


class AccommodationPriceListAdmin (admin.ModelAdmin):
    list_display = ('school_accommodation', 'year')
    inlines = [
        AccommodationPriceInline,
    ]


class CoursePriceListAdmin (admin.ModelAdmin):
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
#admin.site.register(AccommodationPrice) Not needed so far since I have it as inline in the AccommodationPriceList Admin
admin.site.register(AccommodationPriceList, AccommodationPriceListAdmin)
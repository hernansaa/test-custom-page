from django.contrib import admin
from django.db import models

from unfold.admin import ModelAdmin

from django.utils.translation import gettext_lazy as _

from gs_admin.sites import new_admin_site

from unfold.widgets import (UnfoldAdminSplitDateTimeWidget, UnfoldAdminSplitDateTimeVerticalWidget, 
                            UnfoldAdminDateWidget, AdminDateWidget, UnfoldAdminSingleDateWidget,
                            UnfoldAdminTextareaWidget, UnfoldAdminSelectWidget, UnfoldAdminIntegerFieldWidget,
                            UnfoldAdminTextInputWidget)

from .models import (HomePage, AboutUs, ContactPage, TeamMember, StudentReviewsSection,
    WhyUsSection, ContactSection, FeaturedProgramsSection, PopularDestiniesSection,
    HeaderHeroSection, NavbarItem)

# Register your models here.

class NavbarItemInline(admin.StackedInline):
    model = NavbarItem
    extra = 0
    # tab = True

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

class HeaderHeroSectionInline(admin.StackedInline):
    model = HeaderHeroSection
    extra = 0
    max_num = 0 
    # tab = True

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

class PopularDestiniesSectionInline(admin.StackedInline):
    model = PopularDestiniesSection
    extra = 0
    max_num = 0
    # tab = True
    verbose_name = "Popular Destiny"
    verbose_name_plural = "Popular Destinies"
    unfold = True

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

class FeaturedProgramsSectionInline(admin.StackedInline):
    model = FeaturedProgramsSection
    extra = 0
    max_num = 0
    # tab = True
    verbose_name = "Featured Program"
    verbose_name_plural = "Featured Programs"

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

class ContactSectionInline(admin.StackedInline):
    model = ContactSection
    extra = 0
    max_num = 0
    # tab = True
    verbose_name = "Contact"
    verbose_name_plural = "Contact"

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

class StudentReviewsSectionInline(admin.StackedInline):
    model = StudentReviewsSection
    extra = 0
    max_num = 0
    # tab = True
    verbose_name = "Testimonial"
    verbose_name_plural = "Testimonial"

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

class WhyUsSectionInline(admin.StackedInline):
    model = WhyUsSection
    extra = 0
    max_num = 0
    # tab = True
    verbose_name = "Whys?"
    verbose_name_plural = "Why us?"

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


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ['branch']
    inlines = [
        StudentReviewsSectionInline,
        WhyUsSectionInline,
        ContactSectionInline,
        FeaturedProgramsSectionInline,
        PopularDestiniesSectionInline,
        HeaderHeroSectionInline,
        NavbarItemInline,
    ]


@admin.register(HomePage, site=new_admin_site)
class HomePageAdmin(ModelAdmin):
    compressed_fields = True # Unfold Admin Option
    list_display = ['branch']
    inlines = [
        StudentReviewsSectionInline,
        WhyUsSectionInline,
        ContactSectionInline,
        FeaturedProgramsSectionInline,
        PopularDestiniesSectionInline,
        HeaderHeroSectionInline,
        NavbarItemInline,
    ]


    # fieldsets = (
    #         (
    #         _("Student Testimonies"),
    #         {
    #             "classes": ['collapsed in collapse collapse-toggle'],
    #             "fields": [
    #                 # "first_name",
    #                 # "field_4",
    #             ],
    #         },
    #     ),
    # )



class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    extra = 0 

class AboutUsAdmin(admin.ModelAdmin):
    inlines = [TeamMemberInline]
    list_display = ('header_title',)




admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(ContactPage)

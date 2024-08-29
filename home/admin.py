from django.contrib import admin
from django.db import models

from unfold.admin import ModelAdmin, TabularInline, StackedInline

from django.utils.translation import gettext_lazy as _

from gs_admin.sites import new_admin_site

from unfold.widgets import (UnfoldAdminSplitDateTimeWidget, UnfoldAdminSplitDateTimeVerticalWidget, 
                            UnfoldAdminDateWidget, AdminDateWidget, UnfoldAdminSingleDateWidget,
                            UnfoldAdminTextareaWidget, UnfoldAdminSelectWidget, UnfoldAdminIntegerFieldWidget,
                            UnfoldAdminTextInputWidget)

from unfold.contrib.forms.widgets import WysiwygWidget

from .models import (HomePage, AboutUs, ContactPage, TeamMember, StudentReviewsSection,
    WhyUsSection, ContactSection, FeaturedProgramsSection, PopularDestiniesSection,
    HeaderHeroSection, NavbarItem)

from tinymce.models import HTMLField


# DJANGO ADMIN


class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    extra = 0 

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    inlines = [TeamMemberInline]
    list_display = ('header_title',)


class NavbarItemInline(admin.StackedInline):
    model = NavbarItem
    extra = 0


class HeaderHeroSectionInline(admin.StackedInline):
    model = HeaderHeroSection
    extra = 0
    max_num = 0 


class PopularDestiniesSectionInline(admin.StackedInline):
    model = PopularDestiniesSection
    extra = 0
    max_num = 0
    verbose_name = "Popular Destiny"
    verbose_name_plural = "Popular Destinies"
    unfold = True


class FeaturedProgramsSectionInline(admin.StackedInline):
    model = FeaturedProgramsSection
    extra = 0
    max_num = 0
    verbose_name = "Featured Program"
    verbose_name_plural = "Featured Programs"


class ContactSectionInline(admin.StackedInline):
    model = ContactSection
    extra = 0
    max_num = 0
    verbose_name = "Contact"
    verbose_name_plural = "Contact"


class StudentReviewsSectionInline(admin.StackedInline):
    model = StudentReviewsSection
    extra = 0
    max_num = 0
    verbose_name = "Testimonial"
    verbose_name_plural = "Testimonial"


class WhyUsSectionInline(admin.StackedInline):
    model = WhyUsSection
    extra = 0
    max_num = 0
    verbose_name = "Whys?"
    verbose_name_plural = "Why us?"


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


admin.site.register(ContactPage)


# UNFOLD ADMIN


class NavbarItemInline(StackedInline):
    model = NavbarItem
    extra = 0
    # tab = True


class HeaderHeroSectionInline(StackedInline):
    model = HeaderHeroSection
    extra = 0
    max_num = 0 
    # tab = True


class PopularDestiniesSectionInline(StackedInline):
    model = PopularDestiniesSection
    extra = 0
    max_num = 0
    # tab = True
    verbose_name = "Popular Destiny"
    verbose_name_plural = "Popular Destinies"
    unfold = True


class FeaturedProgramsSectionInline(StackedInline):
    model = FeaturedProgramsSection
    extra = 0
    max_num = 0
    # tab = True
    verbose_name = "Featured Program"
    verbose_name_plural = "Featured Programs"


class ContactSectionInline(StackedInline):
    model = ContactSection
    extra = 0
    max_num = 0
    # tab = True
    verbose_name = "Contact"
    verbose_name_plural = "Contact"


class StudentReviewsSectionInline(StackedInline):
    model = StudentReviewsSection
    extra = 0
    max_num = 0
    # tab = True
    verbose_name = "Testimonial"
    verbose_name_plural = "Testimonial"


class WhyUsSectionInline(StackedInline):
    model = WhyUsSection
    extra = 0
    max_num = 0
    # tab = True
    verbose_name = "Whys?"
    verbose_name_plural = "Why us?"


@admin.register(HomePage, site=new_admin_site)
class HomePageAdmin(ModelAdmin):
    compressed_fields = True
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


@admin.register(ContactPage, site=new_admin_site)
class ContactPageAdmin(ModelAdmin):
    compressed_fields = True 


class TeamMemberInline(TabularInline):
    model = TeamMember
    extra = 0 


@admin.register(AboutUs, site=new_admin_site)
class AbouUsAdmin(ModelAdmin):
    compressed_fields = True
    inlines = [TeamMemberInline]
    # list_display = ['branch']

    #Waiting for Issue to be replied in Unfold Github
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
    }

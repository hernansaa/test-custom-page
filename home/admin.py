from django.contrib import admin

from .models import (HomePage, AboutUs, ContactPage, TeamMember, StudentReviewsSection,
    WhyUsSection, ContactSection)

# Register your models here.


class ContactSectionInline(admin.StackedInline):
    model = ContactSection
    extra = 0


class StudentReviwesSectionInline(admin.StackedInline):
    model = StudentReviewsSection
    extra = 1


class WhyUsSectionInline(admin.StackedInline):
    model = WhyUsSection
    extra = 1


class HomePageAdmin(admin.ModelAdmin):
    inlines = [
        StudentReviwesSectionInline,
        WhyUsSectionInline,
        ContactSectionInline,
    ]


admin.site.register(HomePage, HomePageAdmin)


class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    extra = 1

class AboutUsAdmin(admin.ModelAdmin):
    inlines = [TeamMemberInline]
    list_display = ('header_title',)

admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(ContactPage)    
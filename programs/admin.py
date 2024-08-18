from django.contrib import admin
from django.db import models

from gs_admin.sites import new_admin_site

from django.contrib.admin import register

from unfold.admin import ModelAdmin

from .models import (
    CourseType, Include, NotInclude, Requirement,
    Experience, ExperienceIncluded, ExperienceNotIncluded, 
    ExperienceRequirement, ExperienceFaq, Faq
)


class CourseTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


class IncludeAdmin(admin.ModelAdmin):
    list_display = ('include_id', 'description', 'icon')


class NotIncludeAdmin(admin.ModelAdmin):
    list_display = ('not_include_id', 'description', 'icon')


class RequirementAdmin(admin.ModelAdmin):
    list_display = ('requirement_id', 'description')


class ExperienceIncludedInline(admin.TabularInline):
    model = ExperienceIncluded
    extra = 1


class ExperienceNotIncludedInline(admin.TabularInline):
    model = ExperienceNotIncluded
    extra = 1


class ExperienceRequirementInline(admin.TabularInline):
    model = ExperienceRequirement
    extra = 1


class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')


class ExperienceFaqInline(admin.TabularInline):
    model = ExperienceFaq
    extra = 1


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'duration_from_weeks', 'duration_to_weeks', 'allows_work', 'price', 'school', 'course')
    list_filter = ('allows_work', 'city', 'start_date', 'end_date',)
    search_fields = ('name', 'city__name', 'school__name', 'course__name')
    inlines = [
        ExperienceIncludedInline, 
        ExperienceNotIncludedInline, 
        ExperienceRequirementInline,
        ExperienceFaqInline,
        ]
    save_as = True


@register(Experience, site=new_admin_site)
class ExperienceGsAdmin(ModelAdmin):

    compressed_fields = True # Unfold Admin method

    list_display = ('name', 'city', 'duration_from_weeks', 'duration_to_weeks', 'allows_work', 'price', 'school', 'course')
    list_filter = ('allows_work', 'city', 'start_date', 'end_date',)
    search_fields = ('name', 'city__name', 'school__name', 'course__name')
    inlines = [
        ExperienceIncludedInline, 
        ExperienceNotIncludedInline, 
        ExperienceRequirementInline,
        ExperienceFaqInline,
        ]
    save_as = True


admin.site.register(CourseType, CourseTypeAdmin)
admin.site.register(Include, IncludeAdmin)
admin.site.register(NotInclude, NotIncludeAdmin)
admin.site.register(Requirement, RequirementAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Faq, FaqAdmin)


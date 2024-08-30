from django.contrib import admin
from django.contrib.admin import register

from gs_admin.sites import new_admin_site

from unfold.admin import ModelAdmin, TabularInline

from .models import (
    CourseType, Include, NotInclude, Requirement,
    Experience, ExperienceIncluded, ExperienceNotIncluded, ExperienceRequirement,
    ExperienceFaq, Faq
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
   

admin.site.register(CourseType, CourseTypeAdmin)
admin.site.register(Include, IncludeAdmin)
admin.site.register(NotInclude, NotIncludeAdmin)
admin.site.register(Requirement, RequirementAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Faq, FaqAdmin)



# UNFOLD ADMIN


class ExperienceIncludedInline(TabularInline):
    model = ExperienceIncluded
    extra = 0


class ExperienceNotIncludedInline(TabularInline):
    model = ExperienceNotIncluded
    extra = 0


class ExperienceRequirementInline(TabularInline):
    model = ExperienceRequirement
    extra = 0


class ExperienceFaqInline(TabularInline):
    model = ExperienceFaq
    extra = 0


@register(Experience, site=new_admin_site)
class ExperienceGsAdmin(ModelAdmin):
    # Display fields in changeform in compressed mode
    compressed_fields = True
    list_display = ('name', 'city', 'duration_from_weeks', 'duration_to_weeks', 'allows_work', 'price', 'school', 'course')
    list_filter = ('allows_work', 'city', 'start_date', 'end_date',)
    search_fields = ('name', 'city__name', 'school__name', 'course__name')
    list_fullwidth = True
    inlines = [
        ExperienceIncludedInline, 
        ExperienceNotIncludedInline, 
        ExperienceRequirementInline,
        ExperienceFaqInline,
        ]
    save_as = True
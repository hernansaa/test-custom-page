from django.contrib import admin
from django.contrib.admin import register

from unfold.admin import ModelAdmin
from gs_admin.sites import new_admin_site

from .models import AgencyBranch, EmployeeProfile

# DJANGO ADMIN

class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'job_title', 'branch')


admin.site.register(AgencyBranch)
admin.site.register(EmployeeProfile, EmployeeProfileAdmin)


# UNFOLD ADMIN


@register(AgencyBranch, site=new_admin_site)
class AgencyBranchAdmin(ModelAdmin):
    list_display = ('city', 'postal_code', 'telephone', 'info_email', 'web_link')


@register(EmployeeProfile, site=new_admin_site)
class EmployeeProfileAdmin(ModelAdmin):
    list_display = ('user', 'department', 'job_title', 'branch')
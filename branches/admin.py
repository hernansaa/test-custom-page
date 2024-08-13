from django.contrib import admin

from .models import AgencyBranch, EmployeeProfile

# Register your models here.

class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'job_title')


admin.site.register(AgencyBranch)
admin.site.register(EmployeeProfile, EmployeeProfileAdmin)

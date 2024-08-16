from django.contrib import admin

from .models import AboutUs, TeamMember

# Register your models here.

class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    extra = 1

class AboutUsAdmin(admin.ModelAdmin):
    inlines = [TeamMemberInline]
    list_display = ('header_title',)

admin.site.register(AboutUs, AboutUsAdmin)
# admin.site.register(TeamMember) # I think there is no need if it is inline already.
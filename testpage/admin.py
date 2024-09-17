from django.contrib import admin
from django.urls import path

from django.views.generic import TemplateView
from unfold.admin import ModelAdmin
from unfold.views import UnfoldModelAdminViewMixin
from .models import TestPage

from gs_admin.sites import new_admin_site


class MyClassBasedView(UnfoldModelAdminViewMixin, TemplateView):
    title = "Custom Title"  # required: custom page header title
    permission_required = () # required: tuple of permissions
    template_name = "templates/testpage/testpage.html"


@admin.register(TestPage, site=new_admin_site)
class CustomAdmin(ModelAdmin):
    def get_urls(self):
        return super().get_urls() + [
            path(
                "test/",
                MyClassBasedView.as_view(model_admin=self),  # IMPORTANT: model_admin is required
                name="custom_name"
            ),
        ]
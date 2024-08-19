from django.urls import path
from django.views.generic import TemplateView
from unfold.admin import ModelAdmin
from unfold.views import UnfoldModelAdminViewMixin


class MyClassBasedView(UnfoldModelAdminViewMixin, TemplateView):
    title = "Custom Title"  # required: custom page header title
    permissions_required = () # required: tuple of permissions
    template_name = "templates/admin/index.html"


class CustomAdmin(ModelAdmin):
    def get_urls(self):
        return super().get_urls() + [
            path(
                "gs-admin/test/",
                MyClassBasedView.as_view(model_admin=ModelAdmin),  # IMPORTANT: model_admin is required
                name="test"
            ),
        ]
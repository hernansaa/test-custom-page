from django.urls import path

from .sites import new_admin_site

urlpatterns = [
    path("gs-admin/", new_admin_site.urls), # <-- Unfold admin
] 
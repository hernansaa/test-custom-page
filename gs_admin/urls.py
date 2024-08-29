from django.urls import path
from . import views


from .sites import new_admin_site

urlpatterns = [
    path("gs-admin/", new_admin_site.urls), # <-- Unfold admin
    # path('test-admin/', views.index, name='contact_page'),
] 
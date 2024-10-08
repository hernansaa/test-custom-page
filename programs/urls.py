from django.urls import path
from . import views

urlpatterns = [
    path('programs/', views.index, name='programs_index'),
    path('filter-options-by-country/', views.filter_options_by_country, name='filter-options-by-country'),
    path('results-filtered/', views.results_filtered, name='results-filtered'),
    path('programs/program-details/<int:pk>', views.program_details, name='program-details'), 
    path('filter_courses/', views.filter_courses, name='filter_courses'),
    path('update-admin-form/', views.update_admin_form, name='update_admin_form'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('schools/', views.index, name='schools-index'),
    path('schools/school-details/<int:pk>', views.school_details, name='school-details'),
    path('update-course-price/', views.update_course_price, name='update_course_price'),
    path('update-accommodation-price/', views.update_accommodation_price, name='update_accommodation_price'),
    path('update-total-price/', views.update_total_price, name='update_total_price'),
]
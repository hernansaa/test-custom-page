from django.urls import path
from . import views

urlpatterns = [
    path('quotation/<int:id>/update/', views.update_quotation, name='update_quotation'),
    path('quotation/get_schools_by_city/<int:id>', views.get_schools_by_city, name='get_schools_by_city'),
    path('quotation/get_courses_by_school/<int:id>', views.get_courses_by_school, name='get_courses_by_school'),
    path('quotation/get_price_lists_by_course/<int:id>', views.get_price_lists_by_course, name='get_price_lists_by_course'),
    path('quotation/get_course_prices_by_price_list/<int:id>', views.get_course_prices_by_price_list, name='get_course_prices_by_price_list'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('quotation/<int:id>/update/', views.update_quotation, name='update_quotation'),
]
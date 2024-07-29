from django.urls import path
from . import views

urlpatterns = [
    path('providers/', views.index, name='index'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home-index'), # Map the root URL to the index view
]
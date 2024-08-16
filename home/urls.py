from django.urls import path
from django.conf import settings

from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='home_index'),
    path('contact/', views.contact, name='contact_page'),
    path('about-us/', views.about_us, name='about_us')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
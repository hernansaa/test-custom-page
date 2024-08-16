from django.db import models
from tinymce.models import HTMLField


# Create your models here.

class AboutUs(models.Model):
    header_title = models.CharField(max_length=50)
    header_subtitle = models.CharField(max_length=150, null=True, blank=True)
    header_img = models.ImageField(upload_to='home/about_us/header', null=True, blank=True)
    content_title = models.CharField(max_length=50, null=True, blank=True)
    content_subtitle = models.CharField(max_length=150, null=True, blank=True)
    text = HTMLField(null=True, blank=True)

    def __str__(self):
        return f"{self.header_title}"


class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    bio = models.TextField()
    photo = models.ImageField(upload_to='home/about_us/')
    about_us_page = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='team_members')
    
    def __str__(self):
        return self.name
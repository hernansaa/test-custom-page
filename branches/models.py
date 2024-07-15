from django.db import models

from locations.models import City


# Create your models here.

class AgencyBranch(models.Model):
    # id autogenerated by django
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    telephone = models.IntegerField()
    info_email = models.EmailField(max_length=255)
    web_link = models.CharField(max_length=255)

    def __str__(self):
        return self.city_id
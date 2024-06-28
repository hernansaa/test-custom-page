from django.db import models

# Create your models here.

class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    program = models.ForeignKey('programs.Experience', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.name} ({self.email})"

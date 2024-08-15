from django.db import models

from smart_selects.db_fields import ChainedForeignKey

from providers.models import School, Course
from locations.models import City

# Create your models here.

class CourseType(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class Include(models.Model):
    include_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='icons/', null=True, blank=True)

    def __str__(self):
        return self.description

class NotInclude(models.Model):
    not_include_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='icons/', null=True, blank=True)

    def __str__(self):
        return self.description

class Requirement(models.Model):
    requirement_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class Experience(models.Model):
    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]
    
    experience_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    allows_work = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='programs/')
    duration_from_weeks = models.IntegerField()
    duration_to_weeks = models.IntegerField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    min_age = models.IntegerField()
    max_age = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    includes = models.ManyToManyField(Include, through='ExperienceIncluded', related_name='included_in_experiences')
    not_includes = models.ManyToManyField(NotInclude, through='ExperienceNotIncluded', related_name='not_included_in_experiences')
    requirements = models.ManyToManyField(Requirement, through='ExperienceRequirement', related_name='required_in_experiences')
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    course = ChainedForeignKey(
        Course, 
        chained_field="school",
        chained_model_field="school",
        show_all=False,
        auto_choose=False,
        sort=True,
        null=True,
        blank=True,
        )
    
    # school_name = models.CharField(max_length=255)
    # course_type = models.ForeignKey(CourseType, on_delete=models.CASCADE)
    # course_name = models.CharField(max_length=255)
    # course_description = models.TextField()
    # course_weeks_duration = models.IntegerField()
    # course_start_date = models.DateField(null=True, blank=True)
    # course_end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class ExperienceIncluded(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    include = models.ForeignKey(Include, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('experience', 'include')

    def __str__(self):
        return f"{self.experience.name} includes {self.include.description}"

class ExperienceNotIncluded(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    not_include = models.ForeignKey(NotInclude, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('experience', 'not_include')

    def __str__(self):
        return f"{self.experience.name} does not include {self.not_include.description}"

class ExperienceRequirement(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('experience', 'requirement')

    def __str__(self):
        return f"{self.experience.name} requires {self.requirement.description}"

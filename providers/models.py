from django.db import models

from locations.models import City, Country
from branches.models import AgencyBranch
from currencies.models import Currency

# Create your models here.


class Language(models.Model):
    # id autogenerated by django
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Facility(models.Model):
    # id autogenerated by django
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='schools/facilities', null=True, blank=True)

    def __str__(self):
        return self.name
     

class Acreditation(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='providers/acreditations/', null=True, blank=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True, blank=True)
    img = models.ImageField(upload_to='schools/activities', null=True, blank=True)

    def __str__(self):
        return self.name


class Accommodation(models.Model):
    type = models.CharField(max_length=255)
    #name =  models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    img = models.ImageField(upload_to='providers/accommodation/', null=True, blank=True)

    def __str__(self):
        return self.type


class Airport(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name


class Extra(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AvgAge(models.Model):
    from_age = models.IntegerField(null=True, blank=True)
    to_age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"from {self.from_age} to {self.to_age}"
    

class ClassroomEquipment(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='schools/classroom_equipment', null=True, blank=True)

    def __str__(self):
        return self.name


class School(models.Model):
    """
    Main model
    """
    # id autogenerated by django
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE)
    name =  models.CharField(max_length=255)
    short_description = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField()
    img = models.ImageField(upload_to='providers/schools/', null=True, blank=True)
    facilities = models.ManyToManyField(Facility, through='SchoolFacility')
    acreditations = models.ManyToManyField(Acreditation, through='SchoolAcreditation')
    activities = models.ManyToManyField(Activity, through='SchoolActivity')
    airport_transfer = models.ManyToManyField(Airport, through='SchoolAirportTransfer')
    school_equipment = models.ManyToManyField(ClassroomEquipment, through='SchoolClassroomEquipment')
    school_accommodation = models.ManyToManyField(Accommodation, through='SchoolAccommodation')
    extra = models.ManyToManyField(Extra, through='SchoolExtra', blank=True)
    avg_ages = models.ManyToManyField(AvgAge, through='SchoolAvgAge', blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]

    START_DAY_CHOICES = [
        ('monday', 'monday'), ('martes', 'tuesday'), ('miercoles', 'wednesday'),
        ('jueves', 'thursday'), ('viernes', 'friday'), ('sabado', 'saturday'),
        ('domingo', 'sunday')
    ]

    # id autogenerated by django
    name = models.CharField(max_length=255)
    hours_per_week = models.IntegerField(null=True, blank=True)
    lesson_duration_minutes = models.IntegerField(null=True, blank=True)
    course_material = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    max_students = models.IntegerField(null=True, blank=True)
    student_min_age = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    time_table = models.TextField()
    enrollment_fee = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)
    currency = models.CharField(max_length=20, null=True, blank=True)
    start_day = models.CharField(max_length=20, null=True, blank=True, choices=START_DAY_CHOICES, default='monday')
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} | {self.school}"
    

# class CoursePrice(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='prices')
#     weeks = models.PositiveIntegerField()
#     price = models.DecimalField(decimal_places=2, max_digits=6)

#     class Meta:
#        unique_together = ('course', 'weeks')

#     def __str__(self):
#         return f"{self.weeks} semanas ({self.weeks * self.price})"


class CoursePriceList(models.Model):
    """
    Course Price Lists 
    """
    # id autogenerated by django
    year = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.year} : {self.course}"
    

class CoursePrice(models.Model):
    """
    Course Prices
    """
    # id autogenerated by django
    qty_weeks = models.IntegerField(null=True, blank=True)
    week_price_ls = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True) # ls = low season
    week_price_hs = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True) # hs = high season
    week_price_promotional = models.DecimalField(decimal_places=2, max_digits=6)
    course_price_list = models.ForeignKey(CoursePriceList, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
       unique_together = ('course_price_list', 'qty_weeks')

    def __str__(self):
        return f"{self.qty_weeks} semanas"


class Address(models.Model):
    # id autogenerated by django
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    street_number = models.CharField(max_length=20)
    post_code = models.CharField(max_length=20)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f"{self.street}, {self.city.name}"
    

class ContactInformation(models.Model):
    """
    Contact Information for providers.
    
    OneToOne relationship with school and should be ok to use it
    with another providers.
    """
    # id = PK autogenerated by django
    #address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)
    school = models.OneToOneField(School, on_delete=models.CASCADE)
    telephone = models.IntegerField(null=True, blank=True)
    info_email = models.EmailField(max_length=255)
    bookings_email = models.EmailField(max_length=255, null=True, blank=True)
    academics_email = models.EmailField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=254, null=True, blank=True)
    # social_networks = models.ForeignKey(SchoolSocialNetwork, on_delete=models.CASCADE)  VER BIEN DESPUES

    def __str__(self):
        return self.school.name


class SchoolSocialNetwork(models.Model):
    pass


class SchoolImg(models.Model):
    # id autogenerated by django
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='schools/')
    description = models.CharField(max_length=255)
    alt = models.CharField(max_length=255)


class SchoolFacility(models.Model):
    """
    Asociative entity between School and Facility.
    """
    # id autogenerated by django
    facility_id = models.ForeignKey(Facility, on_delete=models.CASCADE)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)


class SchoolAcreditation(models.Model):
    """
    Asociative entity between School and Acreditation.
    """
    # id autogenerated by django
    acreditation_id = models.ForeignKey(Acreditation, on_delete=models.CASCADE)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)


class SchoolActivity(models.Model):
    """
    Asociative entity between School and Activity.
    """
    # id autogenerated by django
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    

class SchoolAccommodation(models.Model):
    """
    Asociative entity between School and Accomodation.
    """
    # id autogenerated by django
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name =  models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.accommodation.type} | {self.name}"


class AccommodationPriceList(models.Model):
    """
    Accommodation Price Lists 
    """
    # id autogenerated by django
    year = models.IntegerField()
    school_accommodation = models.ForeignKey(SchoolAccommodation, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.year} : {self.school_accommodation}"
    

class AccommodationPrice(models.Model):
    """
    Accommodation Prices
    """
    # id autogenerated by django
    qty_weeks = models.IntegerField()
    week_price_ls = models.DecimalField(decimal_places=2, max_digits=6) # ls = low season
    week_price_hs = models.DecimalField(decimal_places=2, max_digits=6) # hs = high season
    week_price_promotional = models.DecimalField(decimal_places=2, max_digits=6)
    accommodation_price_list = models.ForeignKey(AccommodationPriceList, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
       unique_together = ('accommodation_price_list', 'qty_weeks')

    def __str__(self):
        return f"{self.qty_weeks} semanas"


class SchoolAirportTransfer(models.Model):
    """
    Asociative entity between School and Airport.
    """
    YES_NO_CHOICES = [
        ('', 'ida'),
        ('ida/vuelta', 'ida/vuelta')
    ]
    # id autogenerated by django
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name =  models.CharField(max_length=255)
    trip = models.CharField(max_length=12, choices=YES_NO_CHOICES, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6) # ls = low season

    def __str__(self):
        return f"{self.name} ({self.trip}): ({self.price})"


class SchoolExtra(models.Model):
    """
    Asociative entity between School and Extra.
    """
    # id autogenerated by django
    extra = models.ForeignKey(Extra, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    ls_week_price = models.DecimalField(decimal_places=2, max_digits=6) # ls = low season
    hs_week_price = models.DecimalField(decimal_places=2, max_digits=6) # hs = high season


class SchoolAvgAge(models.Model):
    """
    Asociative entity between School and AvgAges? no really many to many
    """
    # id autogenerated by django
    avg_age = models.ForeignKey(AvgAge, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    avg = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)


class SchoolClassroomEquipment(models.Model):
    """
    Asociative entity between School and ClassroomEquipment.
    """
    # id autogenerated by django
    classroom_equipment = models.ForeignKey(ClassroomEquipment, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)


class NationalityMix(models.Model):
    """
    Asociative entity between School and NationalityMix.
    """
    # id autogenerated by django
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    percentage_students = models.DecimalField(max_digits=5, decimal_places=2)  # Maximum 100.00%

    def __str__(self):
        return f"Nationality Mix for {self.country.name}:{self.percentage_students}%"


class SchoolAgencyBranch(models.Model):
    """
    Asociative entity between School and AgencyBranch.
    """
    # id autogenerated by django
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    agency_branch = models.ForeignKey(AgencyBranch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.school}: {self.agency_branch}"
    
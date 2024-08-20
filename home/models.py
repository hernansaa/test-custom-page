from django.db import models

from tinymce.models import HTMLField

from branches.models import AgencyBranch


class HomePage(models.Model):
    header_title = models.CharField(max_length=50)
    header_subtitle = models.CharField(max_length=150, null=True, blank=True)
    header_img_main = models.ImageField(upload_to='home/home/header', null=True, blank=True)
    header_img_first = models.ImageField(upload_to='home/home/header', null=True, blank=True)
    header_img_second = models.ImageField(upload_to='home/home/header', null=True, blank=True)
    header_img_third = models.ImageField(upload_to='home/home/header', null=True, blank=True)
    branch = models.ForeignKey(AgencyBranch, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f"Home Page Global Studies - {self.header_title}"


class StudentReviewsSection(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    profile_img = models.ImageField(upload_to='home/home/reviews', null=True, blank=True)
    review = models.TextField()
    home_page = models.ForeignKey(HomePage, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class WhyUsSection(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    icon_img = models.CharField(max_length=50, null=True, blank=True)
    home_page = models.ForeignKey(HomePage, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class ContactSection(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    sub_title = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='home/home/contact', null=True, blank=True)
    button_first_text = models.CharField(max_length=50, null=True, blank=True)
    button_second_text = models.CharField(max_length=50, null=True, blank=True)
    home_page = models.ForeignKey(HomePage, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"
    

class FeaturedProgramsSection(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    sub_title = models.CharField(max_length=150, null=True, blank=True)
    img = models.ImageField(upload_to='home/home/featured_programs', null=True, blank=True)
    home_page = models.ForeignKey(HomePage, on_delete=models.CASCADE, null=True, blank=True)


class PopularDestiniesSection(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    sub_title = models.CharField(max_length=150, null=True, blank=True)
    img = models.ImageField(upload_to='home/home/popular_destinies', null=True, blank=True)
    home_page = models.ForeignKey(HomePage, on_delete=models.CASCADE, null=True, blank=True)


class HeaderHeroSection(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    sub_title = models.CharField(max_length=150, null=True, blank=True)
    img = models.ImageField(upload_to='home/home/header_hero', null=True, blank=True)
    home_page = models.ForeignKey(HomePage, on_delete=models.CASCADE, null=True, blank=True)


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
    

class ContactPage(models.Model):
    header_title = models.CharField(max_length=50)
    header_subtitle = models.CharField(max_length=150, null=True, blank=True)
    header_img = models.ImageField(upload_to='home/contact/header', null=True, blank=True)
    form_tag = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.header_title}"
    

class NavbarItem(models.Model):
    name = models.CharField(max_length=100) # logo, navbar item, socials, etc.
    text = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, null=True, blank=True)
    img = models.ImageField(upload_to='home/home/navbar', null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    order = models.PositiveIntegerField(default=0, null=True, blank=True)
    visible = models.BooleanField(default=True)
    home_page = models.ForeignKey(HomePage, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


# class FooterContent(models.Model):
#     content = models.TextField()

#     def __str__(self):
#         return "Footer Content" 
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_countries.fields import CountryField
from ckeditor.fields import RichTextField


    

class Tag(models.Model):    
    name = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class HouseApplication(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        )
    
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    house_type = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True)
    status = models.CharField(max_length=200, null=True, blank=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.house_type)


class LegalService(models.Model):
    STATUS = (
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Review', 'Review'),
        )
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    service_type = models.CharField(max_length=200, null=True, blank=True)
    property = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.service_type)
    





class BlogPost(models.Model):
    CATEGORIES = (
        ('Tenancy', 'Tenancy'),
        ('Legal', 'Legal'),
        ('Landlords', 'Landlords'),
    )
    STATUS = (
        ('Published', 'Published'),
        ('Draft', 'Draft'),
        )
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True, choices=STATUS)
    category = models.CharField(max_length=200, null=True, blank=True, choices=CATEGORIES)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("tenancy_post_view", kwargs={"pk": self.pk})
    



class PropertyManagement(models.Model):
    CATEGORY = (
        ('Rent Collected', 'Rent Collected'),
        ('Rent Due', 'Rent Due'),
        ('Rent Overdue', 'Rent Overdue'),
        ('Total Rent', 'Total Rent'),
        )
    

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    Property = models.CharField(max_length=200, null=True)
    PropertyType = models.CharField(max_length=200, null=True)
    PropertyAddress = models.CharField(max_length=200, null=True)
    PropertyCity = models.CharField(max_length=200, null=True)
    NumberOfUnits = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    Rent = models.CharField(null=True, max_length=200, blank=True, choices=CATEGORY)
    RentCollectedDate = models.CharField(max_length=200, null=True)

    def __str__ (self):
        return str(self.Property)
    

class TenantForm(models.Model):

    EMPLOYMENT_CHOICE = (
         ('employed', 'Employed'),
        ('self_employed', 'Self Employed'),
        ('unemployed', 'Unemployed'),
        ('retired', 'Retired'),
        ('student', 'Student'),
        ('other', 'Other'),
    )

    GENDER_CHOICE = (
        ('male', 'Male'),
        ('female', 'Female')

    )

    STATUS = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Completed', 'Completed'),
    )

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True, )
    last_name = models.CharField(max_length=200, null=True, )
    property_name = models.CharField(max_length=200, null=True, )
    country = CountryField(blank_label='(select country)', null=True, )
    phone = models.CharField(max_length=200, null=True, )
    email = models.CharField(max_length=200, null=True, )
    confirm_email = models.CharField(max_length=200, null=True, )
    email_tenant = models.BooleanField(default=False)
    guarantor_details = models.BooleanField(default=False)
    address = models.CharField(max_length=200, null=True)
    employment = models.CharField(max_length=200, null=True, choices=EMPLOYMENT_CHOICE)
    employer = models.CharField(max_length=200, null=True, )
    employer_address = models.CharField(max_length=200, null=True, )
    employer_phone = models.CharField(max_length=200, null=True, )
    job_title = models.CharField(max_length=200, null=True, )
    annual_income = models.CharField(max_length=200, null=True, )
    gender = models.CharField(max_length=200, null=True, choices=GENDER_CHOICE,) 
    status = models.CharField(max_length=200, null=True, blank=True, choices=STATUS, default='Pending')   
    date_of_birth = models.DateField(null=True, )
    smoking = models.BooleanField(default=False, )
    pets = models.BooleanField(default=False, )
    children = models.BooleanField(default=False)

    next_of_kin = models.CharField(max_length=200, null=True)
    next_of_kin_phone = models.CharField(max_length=200, null=True)
    next_of_kin_address = models.CharField(max_length=200, null=True)
    next_of_kin_relationship = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    landlord_name = models.CharField(max_length=200, null=True)
    landlord_phone = models.CharField(max_length=200, null=True)
    landlord_address = models.CharField(max_length=200, null=True)
    landlord_email = models.CharField(max_length=200, null=True)
    

    permission = models.BooleanField(default=False, )
    marketing = models.BooleanField(default=False, )


    def __str__(self):
        return str(self.first_name + ' ' + self.last_name)
    


class Job(models.Model):
    JOBSTATUS = (
        ('Open', 'Open'),
        ('Closed', 'Closed'),
    )
        
    title = models.CharField(max_length=200)
    description = RichTextField(null=True, blank=True)
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True, choices=JOBSTATUS)

    def __str__(self):
        return str(self.title)
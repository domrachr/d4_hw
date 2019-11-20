from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name

class Publisher(models.Model):
    short_name = models.CharField(max_length=254)
    full_name = models.TextField()
    phone_number = PhoneNumberField(null=True, blank=True) 
    country = models.CharField(max_length=2)
    site = models.URLField()

    def __str__(self):
        return self.short_name

class Book(models.Model):  
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True)
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    
    def __str__(self):
        return self.title
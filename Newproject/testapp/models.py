from django.db import models

# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=40)
    email=models.EmailField(max_length=60)
    phonenumber=models.IntegerField()
    coments=models.TextField()

class ContactUs(models.Model):
    username=models.CharField(max_length=50)
    Email=models.EmailField()
    comments = models.TextField()


#Booking Model
class bookModel(models.Model):
    Fullname=models.CharField(max_length=30)
    Email=models.EmailField()
    Phonenumber=models.CharField(max_length=10)
    Booking_date=models.DateField()
    LOCATION_CHOICES = (
        ('HYD', 'Hyderabad'),
    )
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES, default='HYD')



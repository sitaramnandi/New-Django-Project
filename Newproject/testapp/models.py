from django.db import models

# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=40)
    email=models.EmailField(max_length=60)
    
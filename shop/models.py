from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255,unique=True)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=255)
    againpassword=models.CharField(max_length=255)


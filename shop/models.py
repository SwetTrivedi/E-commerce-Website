from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255,unique=True)
    password=models.CharField(max_length=255)
    againpassword=models.CharField(max_length=255)

class UserOTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)  # OTP stored as a string (6 digits)
    created_at = models.DateTimeField(auto_now_add=True)  # When OTP was generated

    def __str__(self):
        return f"{self.user.username} - {self.otp}"
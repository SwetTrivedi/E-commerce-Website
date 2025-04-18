from django.contrib import admin
from .models import UserOTP,Seller
# # Register your models here.
@admin.register(UserOTP)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','user','otp','created_at']

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display=['id','name','email','password','againpassword']



"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup,name='usersignup'),
    path('login/', views.userlogin,name='userlogin'),
    path('userdashboard/', views.userdashboard,name='commondashboard'),
    path('userlogout/', views.user_logout,name='logout'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('seller_page/', views.seller, name='seller'),
    path('sellerdashboard_page/', views.sellerdashboard, name='sellerdash'),
]

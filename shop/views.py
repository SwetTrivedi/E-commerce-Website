from django.shortcuts import render,HttpResponseRedirect,HttpResponse,redirect
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from .models import Customer
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method=="POST":
        # form=Customer(request.POST)
        uname=request.POST.get('name')
        uemail=request.POST.get('email')
        umobile=request.POST.get('mobile')
        upass=request.POST.get('passwd')
        upass2=request.POST.get('passwd2')
        if Customer.objects.filter(email=uemail).exists():
            messages.error(request, "This email is already registered. Please log in.")
        elif upass==upass2:
            myuser=Customer.objects.create(name=uname,email=uemail,mobile=umobile,password=upass,againpassword=upass2)
            myuser.save()
            return HttpResponse("<script>alert('You are registered successfully...')</script>");
        else:
            messages.error(request,"Invalid Password")
    return render(request,'signup.html')

def userdashboard(request):
    return render(request,'userdashboard.html')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            name=request.POST.get('name')
            passwd=request.POST.get('passwd')
            user=authenticate(name=name,password=passwd)
            if user is not None:
                login(request,user)
                return redirect('/commondashboard/')
        # else:
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
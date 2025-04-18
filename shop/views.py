from django.shortcuts import render,HttpResponseRedirect,HttpResponse,redirect
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from.models import Seller
from .forms import OTPForm,Sellersignupform
# from .models import Customer
from django.contrib import messages
from . forms import Signupform , Loginform 
import random
from django.core.mail import send_mail
from .models import UserOTP
# Create your views here.
def home(request):
    return render(request,'home.html')
def generate_otp():
    return str(random.randint(100000, 999999))
def signup(request):
    if request.method == "POST":
        form = Signupform(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.save()

            otp = generate_otp()
            UserOTP.objects.create(user=user, otp=otp)
            send_mail(
                subject='Your OTP for Account Verification',
                message=f'Your OTP is {otp}',
                from_email='your_email@gmail.com',
                recipient_list=[user.email],
            )
            request.session['username'] = user.username  
            messages.success(request, "OTP sent to your email.")
            return redirect('verify_otp') 
    else:
        form = Signupform()
    return render(request, 'signup.html', {'form': form})



def verify_otp(request):
    username = request.session.get('username')
    if not username:
        return redirect('signup')

    form = OTPForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            entered_otp = form.cleaned_data['otp']
            user = User.objects.filter(username=username).first()
            if user:
                real_otp = UserOTP.objects.filter(user=user).first()
                if real_otp and entered_otp == real_otp.otp:
                    user.is_active = True
                    user.save()
                    real_otp.delete()
                    messages.success(request, "OTP verified! You can now login.")
                    return redirect('userlogin')
                else:
                    messages.error(request, "Invalid OTP. Please try again.")

    return render(request, 'verify_otp.html', {'form': form})



def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form=Loginform(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Login Sucessfully !!")
                    return redirect('commondashboard')
        else:
            form=Loginform()
        return render (request,'login.html',{'form':form})
    else:
        return HttpResponseRedirect('/commondashboard/')

def userdashboard(request):
    user=User.objects.filter().first()
    return render(request,'userdashboard.html',{'user':user})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')





###################################################################################################################################################################

def seller(request):
    if request.method == "POST":
        form = Sellersignupform(request.POST)
        if form.is_valid():
            # user = form.save(commit=False) 
            # user.save()
        # if request.method == "POST":
        # form = Sellersignupform(request.POST)
        # if form.is_valid():
            # Check if email already exists in User model
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered.")
                return render(request, 'seller.html', {'form': form})

            # Create User instance if email is not taken
            user = User.objects.create_user(username=form.cleaned_data['name'], 
                                            email=email, 
                                            password=form.cleaned_data['password'])

            # Create Seller instance and link it with the User instance
            seller = form.save(commit=False)
            seller.user = user  # Link Seller with User
            seller.save()



            otp = generate_otp()
            UserOTP.objects.create(user=user, otp=otp)
            send_mail(
                subject='Your OTP for Account Verification',
                message=f'Your OTP is {otp}',
                from_email='your_email@gmail.com',
                recipient_list=[user.email],
            )
            request.session['username'] = user.username 
            messages.success(request, "OTP sent to your email.")
            return redirect('verify_otp') 
    else:
        form = Sellersignupform()
    return render(request, 'seller.html', {'form': form})


def verify_otp(request):
    username = request.session.get('username')
    if not username:
        return redirect('seller')

    form = OTPForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            entered_otp = form.cleaned_data['otp']
            user = Seller.objects.filter(name=username).first()
            if user:
                real_otp = UserOTP.objects.filter(user=user).first()
                if real_otp and entered_otp == real_otp.otp:
                    user.is_active = True
                    user.save()
                    real_otp.delete()
                    messages.success(request, "OTP verified! You can now login.")
                    return redirect('sellerdash')
                else:
                    messages.error(request, "Invalid OTP. Please try again.")

    return render(request, 'verify_otp.html', {'form': form})


def sellerdashboard(request):
    return render(request,'userdashboard.html')


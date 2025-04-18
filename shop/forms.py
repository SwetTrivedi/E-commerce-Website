from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from .models import Seller
from django.utils.translation import gettext,gettext_lazy as _



class Signupform(UserCreationForm):
    password1=forms.CharField(label="Password" ,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label=" Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','email']
        labels={'email':'Email'}

        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'})}



class Loginform(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=_("Password"),
                             strip=False,widget=forms.PasswordInput
                             (attrs={'autocomplete':'current-password','class':'form-control'})) 
    


class OTPForm(forms.Form):
    otp = forms.CharField(
        label="Enter OTP",
        max_length=6,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter 6-digit OTP'})
    )


class Sellersignupform(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['name', 'email', 'password', 'againpassword']
        labels = {'email': 'Email'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'againpassword': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
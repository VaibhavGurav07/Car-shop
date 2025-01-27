from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth.models import User
from .models import Customer


class LoginForm(AuthenticationForm):
    username= forms.CharField()
    password =forms.PasswordInput()




class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField(required=True)
    password1 =forms.PasswordInput( )
    password2 = forms.PasswordInput()

    class Meta:
        model=User
        fields=['username','email','password1','password2']




class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.PasswordInput()
    new_password1 = forms.PasswordInput()
    new_password2 =forms.PasswordInput()





class CustomerProfileForm(forms.ModelForm):
    name = forms.TextInput()
    locality = forms.TextInput()
    city = forms.TextInput()
    mobail = forms.NumberInput()
    state = forms.TextInput()
    zipcode = forms.NumberInput()
    class Meta:
        model = Customer
        fields=['name','locality','city','mobail','state','zipcode']
        # widgets = {
        #     "name" : forms.TextInput(attrs={"class": "form_control"}),
        #     "city" : forms.TextInput(attrs={"class": "form_control"}),
        #     "locality" : forms.TextInput(attrs={"class": "form_control"}),
        #     "mobail": forms.NumberInput(attrs={"class": "form_control"}),
        #     "state" : forms.TextInput(attrs={"class": "form_control"}),
        #     "zipcode" : forms.NumberInput(attrs={"class": "form_control"}),
        # }
        
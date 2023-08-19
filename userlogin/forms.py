from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import AuthenticationForm


class PatientRegistrationForm(UserCreationForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    phone_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    address = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', "type":"email"}))
    gender = forms.ChoiceField(
        choices=[('m', "Male"), ("f", "Female"), ("o", "Other")],
        widget=forms.RadioSelect
    )
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class':"form-control"}))
    height = forms.DecimalField(widget=forms.TextInput(attrs={"type":"number" ,'class':"form-control", "step":"0.1"}))
    weight = forms.DecimalField(widget=forms.TextInput(attrs={"type":"number" ,'class':"form-control", "step":"0.1"}))

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ( 'name', 'username','phone_number', 'address', 'email', 'gender', 'dob', 'height', 'weight', 'password1', 'password2')


class DoctorRegistrationForm(UserCreationForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    phone_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    address = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', "type":"email"}))
    gender = forms.ChoiceField(
        choices=[('m', "Male"), ("f", "Female"), ("o", "Other")],
        widget=forms.RadioSelect
    )
    specialists = forms.ModelMultipleChoiceField(
        queryset=Specialist.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('name','username', 'phone_number', 'address', 'email', 'specialists','gender', 'password1', 'password2')


class DeliveryBoyRegistrationForm(UserCreationForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    phone_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    vehicle_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('name', 'phone_number', 'vehicle_number','username', 'password1', 'password2', )


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
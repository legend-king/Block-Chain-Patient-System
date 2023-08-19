from django import forms
from userlogin.models import Patient
from .models import PatientReport
from django.core.validators import FileExtensionValidator

class PatientProfileForm(forms.ModelForm):
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


    class Meta:
        model = Patient
        fields = ( 'name', 'phone_number', 'address', 'email', 'gender', 'dob', 'height', 'weight')

class PatientReportForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    report_file = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class':"form-control"}),validators=[
            FileExtensionValidator(allowed_extensions=['pdf'])
        ])
    class Meta:
        model=PatientReport
        fields = ('name', 'description', 'report_file')
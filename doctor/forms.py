from django import forms
from userlogin.models import Doctor
from .models import Prescription, PrescribedMedicine
from django.forms import formset_factory



class DoctorProfileForm(forms.ModelForm):
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


    class Meta:
        model = Doctor
        fields = ( 'name', 'phone_number', 'address', 'email', 'gender')


class PrescriptionForm(forms.ModelForm):
    diagnosis = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
    advice = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
    class Meta:
        model = Prescription
        fields = ['diagnosis', 'advice']

class PrescribedMedicineForm(forms.ModelForm):
    medicine_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    MEDICINE_CHOICES = [
        ("t", "Tablet"),
        ("c", "Capsule"),
        ("s", "Syrup"),
    ]
    medicine_type = forms.ChoiceField(
        choices=MEDICINE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    before_breakfast = forms.IntegerField(widget=forms.TextInput(attrs={"type":"number" ,'class':"form-control"}),required=False)
    after_breakfast = forms.IntegerField(widget=forms.TextInput(attrs={"type":"number" ,'class':"form-control"}),required=False)
    before_lunch = forms.IntegerField(widget=forms.TextInput(attrs={"type":"number" ,'class':"form-control"}),required=False)
    after_lunch = forms.IntegerField(widget=forms.TextInput(attrs={"type":"number" ,'class':"form-control"}),required=False)
    before_dinner = forms.IntegerField(widget=forms.TextInput(attrs={"type":"number" ,'class':"form-control"}),required=False)
    after_dinner = forms.IntegerField(widget=forms.TextInput(attrs={"type":"number" ,'class':"form-control"}),required=False)
    evening = forms.IntegerField(widget=forms.TextInput(attrs={"type":"number" ,'class':"form-control"}),required=False)
    tablets = forms.IntegerField(widget=forms.TextInput(attrs={"type":"number" ,'class':"form-control"}))
    duration = forms.IntegerField(widget=forms.TextInput(attrs={"type":"number" ,'class':"form-control"}))
    class Meta:
        model = PrescribedMedicine
        fields = ['medicine_name', 'medicine_type', 'before_breakfast', 'after_breakfast', 'before_lunch', 'after_lunch','evening',  'before_dinner', 'after_dinner', 'tablets', 'duration']

PrescribedMedicineFormSet = formset_factory(PrescribedMedicineForm)
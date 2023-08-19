from django.contrib.auth import login
from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import activate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings

def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            patient = Patient(user=user, name=form.cleaned_data['name'],
                            phone_number=form.cleaned_data['phone_number'],
                            address=form.cleaned_data['address'],
                            email=form.cleaned_data['email'],
                            gender=form.cleaned_data['gender'],
                            dob=form.cleaned_data['dob'],
                            height=form.cleaned_data['height'],
                            weight=form.cleaned_data['weight'])
            patient.save()
            login(request, user)
            return redirect('home')
    else:
        form = PatientRegistrationForm()
    return render(request, 'users/register.html', {'form': form,"register":"Patient Registration","button_text":"Register"})





def register_doctor(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            doctor = Doctor(user=user, name=form.cleaned_data['name'],
                            phone_number=form.cleaned_data['phone_number'],
                            address=form.cleaned_data['address'],
                            email=form.cleaned_data['email'],
                            gender=form.cleaned_data['gender'],
                            )
            doctor.save()
            
            selected_specialist_ids = form.cleaned_data['specialists']

            doctor.specialists.set(selected_specialist_ids)
            
            doctor.save()
            login(request, user)
            return redirect('home')
    else:
        form = DoctorRegistrationForm()
    return render(request, 'users/register.html', {'form': form, "register":"Doctor Registration","button_text":"Register"})


def register_delivery_boy(request):
    if request.method == 'POST':
        form = DeliveryBoyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            delivery_boy = DeliveryBoy(user=user, name=form.cleaned_data['name'],
                                       phone_number=form.cleaned_data['phone_number'],
                                       vehicle_number=form.cleaned_data['vehicle_number'])
            delivery_boy.save()
            login(request, user)
            return redirect('home')
    else:
        form = DeliveryBoyRegistrationForm()
    return render(request, 'users/register.html', {'form': form, "register":"Delivery Boy Registration","button_text":"Register"})



def home(request):
    user = request.user
    is_patient = hasattr(user, 'patient')
    is_doctor = hasattr(user, 'doctor')
    is_delivery_boy = hasattr(user, 'deliveryboy')
    specialists = Specialist.objects.all()

    if is_patient:
        return redirect('patient_profile')
    if is_doctor:
        return redirect('doctor_profile')
    # elif is_consumer:
    #     return redirect('market_place')
    # elif is_delivery_boy:
    #     return redirect('available_orders')

    return render(request, 'home.html', {'is_patient': is_patient, 'is_doctor': is_doctor, 'is_delivery_boy': is_delivery_boy, 'specialists':specialists})


def user_login(request):
    if request.method == 'POST':
        next = request.GET.get('next')
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if next:
                    return redirect(next)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('home')



def set_language(request, language_code):
    if language_code:
        activate(language_code)
        request.session[settings.LANGUAGE_SESSION_KEY] = language_code
    referring_url = request.META.get('HTTP_REFERER', '/')
    response = HttpResponseRedirect(referring_url)
    response.set_cookie('django_language', language_code)

    return response
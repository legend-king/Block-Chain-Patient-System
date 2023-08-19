from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .forms import DoctorProfileForm
from userlogin.models import Doctor
from .forms import PrescriptionForm, PrescribedMedicineForm,PrescribedMedicineFormSet
from django.forms import formset_factory
# Create your views here.

def is_doctor(user):
    return hasattr(user, 'doctor')

@login_required(login_url='login')
@user_passes_test(is_doctor, login_url='login')
def profile(request):
    doctor = Doctor.objects.get(user=request.user)
    return render(request, "doctor/profile.html", {"doctor":doctor, "disp":"profile"})

@login_required(login_url='login')
@user_passes_test(is_doctor, login_url='login')
def edit_profile(request):
    user = get_object_or_404(Doctor, user=request.user)

    if request.method == 'POST':
        form = DoctorProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("doctor_profile")
    else:
        form = DoctorProfileForm(instance=user)

    return render(request, 'users/register.html', {"form": form, "register":"Edit Profile", "button_text":"Edit", "disp":"profile"})

@login_required(login_url='login')
@user_passes_test(is_doctor, login_url='login')
def prescribe_medicine(request,id):
    PrescribedMedicineFormSet = formset_factory(PrescribedMedicineForm, extra=1)

    if request.method == 'POST':
        prescription_form = PrescriptionForm(request.POST)
        prescribed_medicines_formset = PrescribedMedicineFormSet(request.POST, prefix='medicines')
        # print(prescribed_medicines_formset.is_valid())
        # print(prescription_form.is_valid())
        # print(prescribed_medicines_formset)
        if prescription_form.is_valid() and prescribed_medicines_formset.is_valid():
            prescription = prescription_form.save(commit=False)
            prescription.doctor = request.user.doctor
            prescription.patient = User.objects.get(id=id).patient
            prescription.save()
            
            for form in prescribed_medicines_formset:
                prescribed_medicine = form.save(commit=False)
                prescribed_medicine.prescription = prescription
                prescribed_medicine.save()
        return redirect("doctor_profile")
    else:
        prescription_form = PrescriptionForm()
        prescribed_medicines_formset = PrescribedMedicineFormSet(prefix='medicines')
    
    context = {
        'prescription_form': prescription_form,
        'prescribed_medicines_formset': prescribed_medicines_formset,
    }

    return render(request, 'doctor/prescribe_medicine.html', context)
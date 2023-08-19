from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .forms import PatientProfileForm, PatientReportForm
from datetime import datetime
from dateutil.parser import parse
from .models import PatientReport,Patient, Thread
from django.db.models.signals import post_save
from .signals import reportBlockHashCreate
from django.core.paginator import Paginator

from userlogin.models import Doctor, Specialist


post_save.connect(reportBlockHashCreate, PatientReport)
# Create your views here.
def calculate_age(date_of_birth):
    current_date = datetime.now()
    if isinstance(date_of_birth, str):
        date_of_birth = parse(date_of_birth, dayfirst=True)
    age = current_date.year - date_of_birth.year
    if current_date.month < date_of_birth.month or (current_date.month == date_of_birth.month and current_date.day < date_of_birth.day):
        age -= 1
    return age

def calculate_bmr(weight, height, age, gender):
    if gender == 'm' or gender=='o':
        bmr = 66 + (13.75 * weight) + (5 * height) - (6.75 * age)
    elif gender == 'f':
        bmr = 655 + (9.56 * weight) + (1.85 * height) - (4.68 * age)

    return bmr

def is_patient(user):
    return hasattr(user, 'patient')

@login_required(login_url='login')
@user_passes_test(is_patient, login_url='login')
def profile(request):
    patient = Patient.objects.get(user=request.user)
    patient.age=calculate_age(patient.dob)
    patient.bmi = round(patient.weight / ((patient.height/100) ** 2),2)
    patient.bmr=calculate_bmr(float(patient.weight), float(patient.height), int(patient.age), patient.gender)
    
    # Determine weight category based on BMI
    if patient.bmi < 18.5:
        patient.bmi_detail="Underweight"
    elif patient.bmi < 25:
        patient.bmi_detail="Normal Weight"
    elif patient.bmi < 30:
        patient.bmi_detail="Overweight"
    else:
        patient.bmi_detail="Obese"
    return render(request, "patient/profile.html", {"patient":patient, "disp":"profile"})

@login_required(login_url='login')
@user_passes_test(is_patient, login_url='login')
def edit_profile(request):
    user = get_object_or_404(Patient, user=request.user)

    if request.method == 'POST':
        form = PatientProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("patient_profile")
    else:
        form = PatientProfileForm(instance=user)

    return render(request, 'users/register.html', {"form": form, "register":"Edit Profile", "button_text":"Edit", "disp":"profile"})

@login_required(login_url='login')
@user_passes_test(is_patient, login_url='login')
def add_report(request):
    if request.method == 'POST':
        form = PatientReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.patient=request.user.patient
            report.save()
            
            return redirect('patient_report_list')
    else:
        form = PatientReportForm()
    return render(request, 'users/register.html', {'form': form,"register":"Report Upload","button_text":"Upload","disp":"report_upload"})


@login_required(login_url='login')
@user_passes_test(is_patient, login_url='login')
def report_list(request):
    reports = PatientReport.objects.filter(patient=request.user.patient)
    report_per_page = 25
    paginator = Paginator(reports, per_page=report_per_page)
    page_number = request.GET.get('page', 1)
    reports = paginator.get_page(page_number)
    context = {
        'reports': reports,
        'disp':'report_list',
        'check':paginator.count>report_per_page and reports,
    }
    return render(request, 'patient/report_list.html', context=context)

@login_required(login_url='login')
@user_passes_test(is_patient, login_url='login')
def report_view(request, id):
    report = get_object_or_404(PatientReport, patient=request.user.patient, id=id)
    return render(request, 'patient/report_view.html', {"report":report.report_file.url, "disp":"report_list"})


@login_required(login_url='login')
@user_passes_test(is_patient, login_url='login')
def search_doctor(request):
    specialist_ids = request.GET.getlist('specialists')
    
    if specialist_ids:
        doctors = Doctor.objects.filter(specialists__id__in=specialist_ids).distinct().order_by("id")
    else:
        doctors = Doctor.objects.all().order_by("id")

    report_per_page = 25
    paginator = Paginator(doctors, per_page=report_per_page)
    page_number = request.GET.get('page', 1)
    doctors = paginator.get_page(page_number)
    
    specialists = Specialist.objects.all()
    
    return render(request, 'patient/search_doctor.html', {'doctors': doctors, 'specialists': specialists, 
                                                          'check':paginator.count>report_per_page and doctors,
                                                          "selected_specialists":[int(i) for i in specialist_ids],
                                                          "disp":"search_doctor"})


def chat(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads,
        'disp':"chat"
    }
    return render(request, "patient/messages.html", context)


@login_required(login_url='login')
@user_passes_test(is_patient, login_url='login')
def doctor_add(request, id):
    Thread.objects.create(first_person=request.user, second_person=Doctor.objects.get(id=id).user)
    return redirect("patient_doctor_chat")
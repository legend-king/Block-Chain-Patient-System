from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('name','image')
    search_fields = ('name',)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email')
    list_filter = ('gender',)
    search_fields = ('name', 'phone_number', 'email')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email')
    list_filter = ('gender', 'specialists')
    search_fields = ('name', 'phone_number', 'email')
    filter_horizontal = ('specialists',)

@admin.register(DeliveryBoy)
class DeliveryBoyAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'vehicle_number')
    search_fields = ('name', 'phone_number', 'vehicle_number')

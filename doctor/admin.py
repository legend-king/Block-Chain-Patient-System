from django.contrib import admin
from .models import Prescription, PrescribedMedicine
# Register your models here.
@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display=('doctor','patient', 'diagnosis','advice', 'prescribed_on')
    search_fields=('diagnosis', 'advice')
    list_filter=('patient','doctor')


@admin.register(PrescribedMedicine)
class PrescribedMedicineAdmin(admin.ModelAdmin):
    list_display = ('medicine_name', 'medicine_type','tablets', 'duration')
    list_filter=('medicine_type',)
    search_fields=('medicine_name',)
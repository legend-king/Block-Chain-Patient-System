from django.db import models
from django.contrib.auth.models import User
from userlogin.models import Patient, Doctor

# Create your models here.
class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,related_name='prescribed_to')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='prescribed_by')
    diagnosis = models.TextField()
    advice = models.TextField(null=True,blank=True)
    prescribed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription {self.id}"

class PrescribedMedicine(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='medicines')
    medicine_name = models.CharField(max_length=500)
    medicine_type = models.CharField(max_length=50, choices=[("t", "Tablet"), ("c", "Capsule"), ("s", "Syrup")])
    before_breakfast = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    after_breakfast = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    before_lunch = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    after_lunch = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    before_dinner = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    evening = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    after_dinner = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    tablets = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return f"Prescribed Medicine {self.id}"

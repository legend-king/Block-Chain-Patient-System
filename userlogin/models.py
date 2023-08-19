from django.contrib.auth.models import User
from django.db import models

class Specialist(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="specialists")

    def __str__(self):
        return self.name


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email=models.EmailField()
    address = models.TextField()
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=[("m", "Male"),("f", "Female"), ("o", "Other")])
    height = models.DecimalField(decimal_places=2, max_digits=5)
    weight = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    gender = models.CharField(max_length=1, choices=[("m", "Male"),("f", "Female"), ("o", "Other")])
    specialists = models.ManyToManyField(Specialist)

    def __str__(self):
        return self.name
    

class DeliveryBoy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='deliveryboy')
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    vehicle_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
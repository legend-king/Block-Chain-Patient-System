from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.profile, name='doctor_profile'),
    path("edit_profile/", views.edit_profile, name='edit_doctor_profile'),
    path("prescribe_medicine/<int:id>", views.prescribe_medicine, name='doctor_prescribe_medicine'),
]
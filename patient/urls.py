from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.profile, name='patient_profile'),
    path("edit_profile/", views.edit_profile, name='edit_patient_profile'),
    path("report_upload/", views.add_report, name="patient_report_upload"),
    path("report_list/", views.report_list, name="patient_report_list"),
    path("report_view/<int:id>/", views.report_view, name="patient_report_view"),
    path("search_doctor/", views.search_doctor, name="patient_search_doctor"),
    path("chat/", views.chat, name="patient_doctor_chat"),
    path("doctorchat_add/<int:id>", views.doctor_add,name='patient_doctorchat_add'),
]
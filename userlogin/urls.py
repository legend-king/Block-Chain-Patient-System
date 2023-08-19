from django.urls import path
from . import views

urlpatterns = [
    path('register_patient/', views.register_patient, name='register_patient'),
    path('register_doctor/', views.register_doctor, name='register_doctor'),
    path('register_deliveryboy/', views.register_delivery_boy, name='register_delivery_boy'),
    path("", views.home, name="home"),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('set_language/<str:language_code>/', views.set_language, name='set_language'),
]
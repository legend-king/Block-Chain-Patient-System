from django.urls import path
from . import views

urlpatterns = [
    path("new_transaction/", views.new_transaction, name='blockchain_new_transaction'),
    path("chain/", views.get_chain, name='get_chain'),
    
]
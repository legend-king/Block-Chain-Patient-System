from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PatientReport
import requests

ADDR = "http://127.0.0.1:8000/blockchain"

@receiver(post_save, sender=PatientReport)
def reportBlockHashCreate(sender, instance, created, **kwargs):
    if created:
        post_object = {
            "report_id":instance.id,
            "patient": instance.patient.user.username,
            "name" : instance.name,
            "description" : instance.description,
            "report_file" : str(instance.report_file),
        }
        address = "{0}/new_transaction/".format(ADDR)
        requests.post(address, json=post_object)
from django.db import models
from patient.models import PatientReport
# Create your models here.


class PatientBlockModel(models.Model):
    index = models.BigIntegerField()
    transactions = models.ForeignKey(PatientReport,on_delete=models.CASCADE,)
    hash = models.TextField()
    prev_hash = models.TextField()
    nonce=models.IntegerField(default=0)

    def __str__(self):
        return self.hash
    

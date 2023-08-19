from django.contrib import admin
from .models import PatientBlockModel
# Register your models here.
@admin.register(PatientBlockModel)
class PatientBlockModelAdmin(admin.ModelAdmin):
    list_display=("index", "hash", "prev_hash", "nonce")
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('index', 'hash', 'prev_hash', 'nonce',"transactions") 
        else:
            return self.readonly_fields
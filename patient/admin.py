from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(PatientReport)
class PatientReportAdmin(admin.ModelAdmin):
    list_display=('patient','name', 'description','report_file', 'uploaded_at')
    search_fields=('name', )
    list_filter=('patient',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('patient', 'name', 'description', 'report_file',"uploaded_at") 
        else:
            return self.readonly_fields
        


admin.site.register(ChatMessage)

class ChatMessage(admin.TabularInline):
    model = ChatMessage

class ThreadAdmin(admin.ModelAdmin):
    inlines = [ChatMessage]
    class Meta:
        model = Thread


admin.site.register(Thread, ThreadAdmin)
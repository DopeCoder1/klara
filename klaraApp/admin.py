from django.contrib import admin
from .models import *
# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    search_fields = ("service","date","client","timeslot")
    list_display = ("id","service","date","client","timeslot")
    list_filter = ("service","date","client","timeslot")

class ServiceAdmin(admin.ModelAdmin):
    search_fields = ("work_name","price")
    list_display = ("id","work_name","price")
    list_filter = ("work_name","price")

class ClientAdmin(admin.ModelAdmin):
    search_fields = ("id","user")
    list_display = ("id","user")
    list_filter = ("id","user")

class WorksAdmin(admin.ModelAdmin):
    search_fields = ("id","name")
    list_display = ("id","name")
    list_filter = ("id","name")

admin.site.register(Appointment,AppointmentAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(ClientProfile,ClientAdmin)
admin.site.register(Works,WorksAdmin)

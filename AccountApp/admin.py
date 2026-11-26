from django.contrib import admin
from .models import *
from AppointmentApp.models import Appointment


# Register your models here.
admin.site.register(User)

#class AppointmentStacked(admin.TabularInline):

class AppointmentStacked(admin.StackedInline):
    model=Appointment
    extra=1
class DoctorPersoClass(admin.ModelAdmin):
    inlines=[AppointmentStacked]
admin .site.register(Doctor, DoctorPersoClass)

admin.site.register(Patient)
admin.site.register(Speciality)
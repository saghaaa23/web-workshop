from django.contrib import admin
from .models import Appointment
# Register your models here.
#admin.site.register(Appointment)
# Register your models here.
# admin.site.register(Appointment)
 
# class AppointmentAdminPers(admin.ModelAdmin):
#     list_display=("reason","status","duration_minutes","appointment_date")
# admin.site.register(Appointment,AppointmentAdminPers)

@admin.action(description="Maake them confirmed")
def confirmed_appointments(model, req, queryset):
    queryset.update(status='CONFIRMED') 



@admin.register(Appointment)
class AppointmentAdminPers(admin.ModelAdmin):
    actions=[confirmed_appointments]
    list_display=('reason', 'status', 'appointment_date', 'doctor', 'patient')
    list_filter=('status', 'appointment_date', 'doctor', 'patient')
    list_editable=('status',)
    search_fields=('status','reason')
    ordering=('-appointment_date',)
    list_per_page= 2
    fieldsets=(
        ('Description',{
            'fields':('reason','prescription','status')
        }),
        ('Date + Duration',{
            'fields':('appointment_date','duration_minutes')
        }),
        ('Patients / Doctors',{
            'fields':('doctor','patient')
        }),
        ('Planification',{
            'fields':('created_at','updated_at')
    
        })
    )
    readonly_fields=('created_at','updated_at')
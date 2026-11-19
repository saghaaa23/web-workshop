from django.db import models
from AccountApp.models import Doctor,Patient

# Create your models here.q
class Appointment(models.Model):
    reason=models.TextField()
    prescription=models.FieldField(
        blank=True,
        upload_to='prescriptions/',
    )
class Status(models.TextChoices):
    PENDING='PENDING'"En attente"
    CONFIRMED='CONFIRMED'"Confirmé"
    CANCELLED='CANCELLED'"Annulé"
    Status=models.CharField(max_length=10,choices=Status.choices,
                            default=Status.PENDING)
   # Status=models.CharField(max_length=10,choices=[("PENDING","En attente","CONFIRMED","Confirmé","CANCELLED","Annulé")],default=Status.PENDING)
    duration_minutes= models.PositiveBigIntegerField(default=30)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    Appointment_date=models.DateTimeField()
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='appointments')
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='appointments')
    #patient=models.ForeignKey('AccountApp.Patient',on_delete=models.CASCADE,related_name='appointments')
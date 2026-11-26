from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone


class Appointment(models.Model):

    class Status(models.TextChoices):
        PENDING = 'PENDING', 'En attente'
        CONFIRMED = 'CONFIRMED', 'Confirmé'
        CANCELLED = 'CANCELLED', 'Annulé'

    reason = models.TextField()
    prescription = models.FileField(
        upload_to='prescriptions/',
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )
    duration_minutes = models.PositiveIntegerField(default=30)
    appointment_date = models.DateTimeField()
    doctor = models.ForeignKey('AccountApp.Doctor', on_delete=models.CASCADE,
                               related_name='appointments')
    patient = models.ForeignKey('AccountApp.Patient', on_delete=models.CASCADE,
                                related_name='appointments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['appointment_date']
        constraints = [
            models.UniqueConstraint(
                fields=['doctor', 'appointment_date'],
                name='unicite_doctor_appointment_date',
                violation_error_message='Doctor already has an appointment at this date and time.',
            )
        ]

    def clean(self):
        super().clean()
        if self.appointment_date is None:
            return  

        date_modified = self._state.adding or not Appointment.objects.filter(
            pk=self.pk, appointment_date=self.appointment_date
        ).exists()

        if date_modified and self.appointment_date <= timezone.now():
            raise ValidationError(
                {'appointment_date': "Appointment date must be in the future."}
            )

        def __str__(self):
            return f"Le rdv est pour la raison{self.reason}"

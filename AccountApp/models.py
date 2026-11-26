from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError


# ---- Validators (barra el classes, fou9) ----
number_validation = RegexValidator(
    regex=r'^\d{8}$',
    message='national id must be exactly 8 digits.'
)

def validate_birth_date(value):
    if value >= timezone.localdate():
        raise ValidationError("birth date must be in the past")


# ---- Models ----
class User(AbstractUser):
    pass


class Speciality(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Speciality"
        verbose_name_plural = "Specialities"

    def __str__(self):
        return self.name

class Doctor(User):
    licence_number = models.CharField(
        max_length=6, unique=True,
        validators=[MinLengthValidator(6), MaxLengthValidator(6)]
    )
    phone_number = models.CharField(max_length=8)
    specialities = models.ManyToManyField(Speciality, related_name="doctors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
            verbose_name = "Doctor"
            verbose_name_plural = "Doctors"


class Patient(User):
    national_id = models.CharField(max_length=8, unique=True, validators=[number_validation])
    phone_number = models.CharField(max_length=8)
    birth_date = models.DateField(validators=[validate_birth_date])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
                verbose_name = "Patient"
                verbose_name_plural = "Patients"
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator , MaxLengthValidator , RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.
class User(AbstractUser):

    pass
class Speciality(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Doctor(User):
    licence_number = models.CharField(max_length=6, unique=True,validators=[MinLengthValidator(6),MaxLengthValidator(6)])
    phone_number = models.CharField(max_length=8)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    #specialities=models.ManyToManyField (AppAccount.'Speciality')
    specialities=models.ManyToManyField (
        Speciality, related_name="doctors"
        )
    number_validation = RegexValidator(regex=r'^\d{8}$', message='national id must be exactly 8 digit.')

    def validate_birth_date(value):
        if value >= timezone.localdatedate():
            raise ValidationError("birth date must be in the pasttttt")
class Patient(User):
    national_id = models.CharField(max_length=9, unique=True,validators='number_validation')                                     
    phone_number = models.CharField(max_length=8)
    birth_date = models.DateField(validators=[validate_birth_date])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)




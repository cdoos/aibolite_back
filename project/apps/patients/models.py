from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Patient(models.Model):
    user = models.OneToOneField(
        'users.User',
        verbose_name=_('User'),
        related_name='patient',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    blood_group = models.IntegerField(
        verbose_name=_('Blood group'),
        blank=True,
        null=True
    )
    emergency_contact_number = PhoneNumberField(
        verbose_name=_('Emergency contact number'),
        max_length=12,
        unique=True,
        blank=True,
        null=True
    )
    email = models.EmailField(
        verbose_name=_('email'),
        blank=True,
        null=True
    )
    address = models.CharField(
        verbose_name=_('Address'),
        max_length=100
    )
    marital_status = models.CharField(
        verbose_name=_('Marital status'),
        max_length=100
    )
    registration_date = models.DateTimeField(
        verbose_name=_('Registration date'),
        null=True,
        blank=True
    )


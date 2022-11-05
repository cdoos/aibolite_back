from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    iin = models.CharField(
        verbose_name=_('IIN'),
        max_length=12,
        blank=True
    )
    first_name = models.CharField(
        verbose_name=_('first name'),
        max_length=30
    )
    last_name = models.CharField(
        verbose_name=_('last name'),
        max_length=30,
        blank=True
    )
    middle_name = models.CharField(
        verbose_name=_('middle name'),
        max_length=30,
        blank=True
    )
    contact_number = PhoneNumberField(
        max_length=12,
        unique=True,
        blank=True
    )

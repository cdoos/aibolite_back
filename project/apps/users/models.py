from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from .managers import UserManager


class User(AbstractBaseUser):
    username = models.CharField(
        verbose_name=_("Username"),
        max_length=20
    )
    date_of_birth = models.DateField(
        verbose_name=_("Date of Birth"),
    )
    iin = models.CharField(
        verbose_name=_('IIN'),
        max_length=12,
        blank=True,
    )
    first_name = models.CharField(
        verbose_name=_('first name'),
        max_length=30,
    )
    last_name = models.CharField(
        verbose_name=_('last name'),
        max_length=30,
        blank=True,
    )
    middle_name = models.CharField(
        verbose_name=_('middle name'),
        max_length=30,
        blank=True,
        null=True,
    )
    contact_number = PhoneNumberField(
        max_length=12
    )
    address = models.CharField(
        verbose_name=_('Address'),
        max_length=100,
        blank=True,
    )

    objects = UserManager()

    EMAIL_FIELD = 'username'
    USERNAME_FIELD = 'username'

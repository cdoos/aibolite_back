from django.db import models
from django.utils.translation import gettext_lazy as _
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFit


class Doctor(models.Model):
    class CATEGORY(models.IntegerChoices):
        HIGHEST = 0, _("Highest")
        FIRST = 1, _("First")
        SECOND = 2, _("Second")
        THIRD = 3, _("Third")
        FOURTH = 4, _("Fourth")

    class DEGREE(models.IntegerChoices):
        BACHELORS = 0, _("Bachelors")
        MASTERS = 1, _("Masters")
        PHD = 3, _("PHD")
        DOCTORATE = 4, _("Doctorate")

    user = models.OneToOneField(
        'users.User',
        verbose_name=_('User'),
        related_name='doctor',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    department_id = models.SmallIntegerField(
        verbose_name=_("Department ID"),
    )
    specialization_details_id = models.SmallIntegerField(
        verbose_name=_("Specialization Details ID"),
    )
    experience_in_years = models.SmallIntegerField(
        verbose_name=_("Experience in years"),
    )
    photo = ProcessedImageField(
        verbose_name=_("Photo"),
        upload_to="doctor/photos/",
        null=True,
        blank=True,
        format="JPEG",
        options={"quality": 90},
        processors=[
            ResizeToFit(width=1920, height=1200, upscale=False),  # max-width
        ],
    )
    category = models.PositiveSmallIntegerField(
        verbose_name=_("Category"),
        choices=CATEGORY.choices,
        default=CATEGORY.FOURTH,
    )
    price_per_appointment = models.DecimalField(
        verbose_name=_("Price Per Appointment"),
        max_digits=9,
        decimal_places=2,
    )
    schedule_details = models.CharField(
        verbose_name=_("Schedule Details"),
        max_length=256,
    )
    degree = models.PositiveSmallIntegerField(
        verbose_name=_("Degree"),
        choices=DEGREE.choices,
        default=DEGREE.PHD,
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name=_("Rating"),
        default=0,
    )
    homepage_url = models.CharField(
        verbose_name="Homepage URL",
        null=True,
        blank=True,
    )

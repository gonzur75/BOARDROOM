
from django.core.validators import MinValueValidator
from django.db import models
from home.validators import date_validator

# Create your models here.
from django.utils import timezone


class Boardrooms(models.Model):
    name = models.CharField(max_length=255, unique=True,
                            error_messages={"unique": "This name already exist"})
    capacity = models.IntegerField(validators=[MinValueValidator(0, message="Use positive number only")])
    projector = models.BooleanField(null=True)


class Reservations(models.Model):
    rese_date = models.DateField(verbose_name="Reservation date", default=timezone.now(), validators=[date_validator])
    comment = models.TextField()
    boardrooms = models.ForeignKey(Boardrooms, on_delete=models.CASCADE, related_name="reservations")

    class Meta:
        unique_together = ('rese_date', 'boardrooms')


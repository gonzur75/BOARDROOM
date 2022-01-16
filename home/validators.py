from django.core.exceptions import ValidationError
from django.utils.datetime_safe import date


def date_validator(value):
    if value < date.today():
        raise ValidationError("Only future date")

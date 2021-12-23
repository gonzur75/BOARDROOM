from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Boardrooms(models.Model):
    name = models.CharField(max_length=255, unique=True,
                            error_messages={"unique": "This name already exist"})
    capacity = models.IntegerField(validators=[MinValueValidator(0, message="Use positive number only")])
    projector = models.BooleanField(null=True)


class Reservations(models.Model):
    rese_date = models.DateField()
    comment = models.TextField()
    boardrooms = models.ForeignKey('Boardrooms', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('rese_date', 'boardrooms')


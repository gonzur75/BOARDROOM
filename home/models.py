from django.db import models

# Create your models here.


class Boardrooms(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField()
    projector = models.BooleanField(null=True)

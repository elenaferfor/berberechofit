from django.conf import settings
from django.db import models
from django.utils import timezone


class Activity(models.Model):
    name = models.CharField(max_length=100)
    max_seats =models.IntegerField () 
    description = models.CharField(null=True, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)

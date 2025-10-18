from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Activity(models.Model):
    name = models.CharField(max_length=100)
    max_seats =models.IntegerField () 
    description = models.CharField(null=True, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    

class Inscripcion(models.Model):
    usuario = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="inscripciones")
    inscription_date = models.DateTimeField(auto_now_add=True)
    available_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('usuario', 'actividad')

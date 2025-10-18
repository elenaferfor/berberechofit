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
    
    @property
    def inscritos_count(self):
        return self.inscripciones.count()
    
    @property
    def seats_left(self):
        return self.max_seats - self.inscritos_count


    def clean(self):
        if self.inscritos_count > self.max_participantes:
            raise ValidationError("Se ha alcanzado el número máximo de participantes.")

class Inscripcion(models.Model):
    usuario = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="inscripciones")
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'actividad')

    def clean(self):
        if self.actividad.inscritos_count >= self.actividad.max_participantes:
            raise ValidationError("No se pueden registrar más usuarios en esta actividad.")

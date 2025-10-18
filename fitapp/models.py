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

    def clean(self):
        # Validación para que no se pueda exceder el máximo de participantes
        if self.inscritos_count > self.max_participantes:
            raise ValidationError("Se ha alcanzado el número máximo de participantes.")

class Inscripcion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="inscripciones")
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'actividad')  # evita que un usuario se registre dos veces

    def clean(self):
        if self.actividad.inscritos_count >= self.actividad.max_participantes:
            raise ValidationError("No se pueden registrar más usuarios en esta actividad.")

    def __str__(self):
        return f"{self.usuario.username} inscrito en {self.actividad.nombre}"

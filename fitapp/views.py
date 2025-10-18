from django.shortcuts import render
from .models import Inscripcion, Activity

def inscriptions(request):

    available_inscriptions = Inscripcion.objects.filter(usuario__isnull=True)
    not_available_inscriptions = Inscripcion.objects.filter(usuario__isnull=False)

    
    return render(request, 'fitapp/index.html', {'available_inscriptions': available_inscriptions, 'not_available_inscriptions': not_available_inscriptions})

def inscription_detail(request, pk):
    inscription = Inscripcion.objects.get(pk=pk)
    return render(request, 'fitapp/actividad.html', {'inscription': inscription})
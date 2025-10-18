from django.shortcuts import render

def inscriptions(request):
    return render(request, 'fitapp/index.html', {})

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inscriptions, name='incriptions'),
]
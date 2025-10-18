from django.urls import path
from . import views

urlpatterns = [
    path('', views.inscriptions, name='incriptions'),
    path('inscription/<int:pk>/', views.inscription_detail, name='inscription_detail'),
]
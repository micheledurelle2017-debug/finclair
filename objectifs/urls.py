from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_objectifs, name='liste_objectifs'),
    path('ajouter/', views.ajouter_objectif, name='ajouter_objectif'),
]
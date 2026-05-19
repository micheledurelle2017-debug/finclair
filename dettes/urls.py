from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_dettes, name='liste_dettes'),
    path('ajouter/', views.ajouter_dette, name='ajouter_dette'),
    path('rembourser/<int:pk>/', views.rembourser_dette, name='rembourser_dette'),
]
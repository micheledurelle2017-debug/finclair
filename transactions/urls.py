from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_transactions, name='liste_transactions'),
    path('ajouter/', views.ajouter_transaction, name='ajouter_transaction'),
    path('supprimer/<int:pk>/', views.supprimer_transaction, name='supprimer_transaction'),
]
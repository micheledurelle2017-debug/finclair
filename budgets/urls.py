from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_budgets, name='liste_budgets'),
    path('ajouter/', views.ajouter_budget, name='ajouter_budget'),
]
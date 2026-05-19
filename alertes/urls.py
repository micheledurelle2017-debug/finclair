from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_alertes, name='liste_alertes'),
    path('lire/<int:pk>/', views.marquer_lu, name='marquer_lu'),
]
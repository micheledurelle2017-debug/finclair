from django.contrib import admin
from .models import Objectif

@admin.register(Objectif)
class ObjectifAdmin(admin.ModelAdmin):
    list_display = ['titre', 'montant_cible', 'montant_actuel', 'date_cible', 'utilisateur']
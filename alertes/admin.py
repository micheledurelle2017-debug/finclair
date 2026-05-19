from django.contrib import admin
from .models import Alerte

@admin.register(Alerte)
class AlerteAdmin(admin.ModelAdmin):
    list_display = ['titre', 'type_alerte', 'lu', 'date_creation', 'utilisateur']
    list_filter = ['type_alerte', 'lu']
from django.contrib import admin
from .models import Dette

@admin.register(Dette)
class DetteAdmin(admin.ModelAdmin):
    list_display = ['titre', 'montant', 'type_dette', 'personne', 'date_echeance', 'rembourse']
    list_filter = ['type_dette', 'rembourse']
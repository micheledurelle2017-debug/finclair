from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['titre', 'montant', 'type_transaction', 'categorie', 'date', 'utilisateur']
    list_filter = ['type_transaction', 'categorie']
    search_fields = ['titre', 'description']
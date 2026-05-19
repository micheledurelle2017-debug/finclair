import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from transactions.models import Transaction

@login_required
def statistiques(request):
    # Dépenses par catégorie
    depenses_cat = Transaction.objects.filter(
        utilisateur=request.user,
        type_transaction='depense'
    ).values('categorie').annotate(total=Sum('montant'))

    # Revenus vs dépenses par mois
    from django.db.models.functions import TruncMonth
    revenus_mois = Transaction.objects.filter(
        utilisateur=request.user,
        type_transaction='revenu'
    ).annotate(mois=TruncMonth('date')).values('mois').annotate(
        total=Sum('montant')
    ).order_by('mois')

    depenses_mois = Transaction.objects.filter(
        utilisateur=request.user,
        type_transaction='depense'
    ).annotate(mois=TruncMonth('date')).values('mois').annotate(
        total=Sum('montant')
    ).order_by('mois')

    mois_labels = json.dumps([
        str(item['mois'].strftime('%b %Y')) for item in revenus_mois
    ])
    revenus_data = json.dumps([float(item['total']) for item in revenus_mois])
    depenses_data = json.dumps([float(item['total']) for item in depenses_mois])

    cat_labels = json.dumps([item['categorie'] for item in depenses_cat])
    cat_data = json.dumps([float(item['total']) for item in depenses_cat])

    return render(request, 'statistiques/statistiques.html', {
        'mois_labels': mois_labels,
        'revenus_data': revenus_data,
        'depenses_data': depenses_data,
        'cat_labels': cat_labels,
        'cat_data': cat_data,
    })
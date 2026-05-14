from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Transaction

@login_required  # Redirige vers connexion si pas connecté
def liste_transactions(request):
    # Récupère uniquement les transactions de l'utilisateur connecté
    transactions = Transaction.objects.filter(
        utilisateur=request.user
    ).order_by('-date')
    return render(request, 'transactions/liste.html', {
        'transactions': transactions
    })

@login_required
def ajouter_transaction(request):
    if request.method == 'POST':
        Transaction.objects.create(
            utilisateur=request.user,
            titre=request.POST['titre'],
            montant=request.POST['montant'],
            type_transaction=request.POST['type_transaction'],
            categorie=request.POST['categorie'],
            description=request.POST.get('description', '')
        )
        return redirect('liste_transactions')
    return render(request, 'transactions/ajouter.html')

@login_required
def supprimer_transaction(request, pk):
    # get_object_or_404 : retourne erreur 404 si non trouvé
    transaction = get_object_or_404(
        Transaction, pk=pk, utilisateur=request.user
    )
    transaction.delete()
    return redirect('liste_transactions')
import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from transactions.models import Transaction
from budgets.models import Budget
from objectifs.models import Objectif

@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(
        utilisateur=request.user
    ).order_by('-date')[:5]

    revenus = Transaction.objects.filter(
        utilisateur=request.user, type_transaction='revenu'
    ).aggregate(total=Sum('montant'))['total'] or 0

    depenses = Transaction.objects.filter(
        utilisateur=request.user, type_transaction='depense'
    ).aggregate(total=Sum('montant'))['total'] or 0

    solde = revenus - depenses

    depenses_par_cat = Transaction.objects.filter(
        utilisateur=request.user, type_transaction='depense'
    ).values('categorie').annotate(total=Sum('montant'))

    categories_labels = json.dumps([item['categorie'] for item in depenses_par_cat])
    categories_data = json.dumps([float(item['total']) for item in depenses_par_cat])

    return render(request, 'users/dashboard.html', {
        'transactions': transactions,
        'solde': float(solde),
        'revenus': float(revenus),
        'depenses': float(depenses),
        'categories_labels': categories_labels,
        'categories_data': categories_data,
    })

def inscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'users/inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'users/connexion.html', {'form': form})

def deconnexion(request):
    logout(request)
    return redirect('connexion')
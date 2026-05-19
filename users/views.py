from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from transactions.models import Transaction
from budgets.models import Budget
from objectifs.models import Objectif
from .models import Profil

@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(
        utilisateur=request.user
    ).order_by('-date')[:5]  # Les 5 dernières seulement

    # Calcul du solde total
    revenus = sum(t.montant for t in Transaction.objects.filter(
        utilisateur=request.user, type_transaction='revenu'
    ))
    depenses = sum(t.montant for t in Transaction.objects.filter(
        utilisateur=request.user, type_transaction='depense'
    ))
    solde = revenus - depenses

    return render(request, 'users/dashboard.html', {
        'transactions': transactions,
        'solde': solde,
        'revenus': revenus,
        'depenses': depenses,
    })

def inscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connecte automatiquement après inscription
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

@login_required
def profil(request):
    profil, created = Profil.objects.get_or_create(utilisateur=request.user)
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email = request.POST.get('email', '')
        request.user.save()
        profil.telephone = request.POST.get('telephone', '')
        profil.save()
        return redirect('profil')
    return render(request, 'users/profil.html', {'profil': profil})
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Budget

@login_required
def liste_budgets(request):
    budgets = Budget.objects.filter(utilisateur=request.user)
    return render(request, 'budgets/liste.html', {'budgets': budgets})

@login_required
def ajouter_budget(request):
    if request.method == 'POST':
        Budget.objects.create(
            utilisateur=request.user,
            categorie=request.POST['categorie'],
            limite=request.POST['limite'],
            mois=request.POST['mois']
        )
        return redirect('liste_budgets')
    return render(request, 'budgets/ajouter.html')
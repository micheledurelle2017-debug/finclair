from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Alerte

@login_required
def liste_alertes(request):
    alertes = Alerte.objects.filter(
        utilisateur=request.user
    ).order_by('-date_creation')
    alertes_non_lues = alertes.filter(lu=False).count()
    return render(request, 'alertes/liste.html', {
        'alertes': alertes,
        'alertes_non_lues': alertes_non_lues,
    })

@login_required
def marquer_lu(request, pk):
    alerte = get_object_or_404(Alerte, pk=pk, utilisateur=request.user)
    alerte.lu = True
    alerte.save()
    return redirect('liste_alertes')
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Objectif

@login_required
def liste_objectifs(request):
    objectifs = Objectif.objects.filter(utilisateur=request.user)
    return render(request, 'objectifs/liste.html', {'objectifs': objectifs})

@login_required
def ajouter_objectif(request):
    if request.method == 'POST':
        Objectif.objects.create(
            utilisateur=request.user,
            titre=request.POST['titre'],
            montant_cible=request.POST['montant_cible'],
            date_cible=request.POST['date_cible'],
            description=request.POST.get('description', '')
        )
        return redirect('liste_objectifs')
    return render(request, 'objectifs/ajouter.html')
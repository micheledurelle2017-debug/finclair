from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Dette

@login_required
def liste_dettes(request):
    dettes = Dette.objects.filter(utilisateur=request.user).order_by('date_echeance')
    total_emprunte = sum(d.montant for d in dettes if d.type_dette == 'emprunt' and not d.rembourse)
    total_prete = sum(d.montant for d in dettes if d.type_dette == 'pret' and not d.rembourse)
    return render(request, 'dettes/liste.html', {
        'dettes': dettes,
        'total_emprunte': total_emprunte,
        'total_prete': total_prete,
    })

@login_required
def ajouter_dette(request):
    if request.method == 'POST':
        Dette.objects.create(
            utilisateur=request.user,
            titre=request.POST['titre'],
            montant=request.POST['montant'],
            type_dette=request.POST['type_dette'],
            personne=request.POST['personne'],
            date_echeance=request.POST['date_echeance'],
            description=request.POST.get('description', '')
        )
        return redirect('liste_dettes')
    return render(request, 'dettes/ajouter.html')

@login_required
def rembourser_dette(request, pk):
    dette = get_object_or_404(Dette, pk=pk, utilisateur=request.user)
    dette.rembourse = True
    dette.save()
    return redirect('liste_dettes')
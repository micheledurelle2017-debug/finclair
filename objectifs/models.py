from django.db import models
from django.contrib.auth.models import User

class Objectif(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    montant_cible = models.DecimalField(max_digits=10, decimal_places=2)
    montant_actuel = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_cible = models.DateField()
    description = models.TextField(blank=True)

    def progression(self):
        return (self.montant_actuel / self.montant_cible) * 100

    def __str__(self):
        return f"{self.titre} - {self.progression():.0f}%"
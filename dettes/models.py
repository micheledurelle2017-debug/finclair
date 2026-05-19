from django.db import models
from django.contrib.auth.models import User

class Dette(models.Model):
    TYPE_CHOICES = [
        ('emprunt', 'J\'ai emprunté'),
        ('pret', 'J\'ai prêté'),
    ]

    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    type_dette = models.CharField(max_length=10, choices=TYPE_CHOICES)
    personne = models.CharField(max_length=200)
    date_echeance = models.DateField()
    rembourse = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.titre} - {self.montant} FCFA"
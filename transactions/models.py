from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    TYPE_CHOICES = [
        ('revenu', 'Revenu'),
        ('depense', 'Dépense'),
    ]

    CATEGORIE_CHOICES = [
        ('alimentation', 'Alimentation'),
        ('transport', 'Transport'),
        ('logement', 'Logement'),
        ('sante', 'Santé'),
        ('loisirs', 'Loisirs'),
        ('education', 'Éducation'),
        ('autres', 'Autres'),
    ]

    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    type_transaction = models.CharField(max_length=10, choices=TYPE_CHOICES)
    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.titre} - {self.montant} FCFA"
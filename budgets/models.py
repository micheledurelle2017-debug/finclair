from django.db import models
from django.contrib.auth.models import User

class Budget(models.Model):
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
    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES)
    limite = models.DecimalField(max_digits=10, decimal_places=2)
    mois = models.DateField()

    def __str__(self):
        return f"{self.categorie} - {self.limite} FCFA"
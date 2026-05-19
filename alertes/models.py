from django.db import models
from django.contrib.auth.models import User

class Alerte(models.Model):
    TYPE_CHOICES = [
        ('budget', 'Dépassement budget'),
        ('objectif', 'Objectif atteint'),
        ('dette', 'Échéance dette'),
    ]

    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    message = models.TextField()
    type_alerte = models.CharField(max_length=20, choices=TYPE_CHOICES)
    lu = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titre} - {self.type_alerte}"
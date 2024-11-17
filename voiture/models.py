# cars/models.py
from django.db import models

class Car(models.Model):
    matricule = models.CharField(max_length=100)
    marque = models.CharField(max_length=100)
    kilometrage = models.PositiveIntegerField()
    prix_jours = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilite = models.CharField(max_length=10, choices=[('louer', 'Louer'), ('parc', 'Parc')])

    def __str__(self):
        return f"{self.matricule} - {self.marque}"

       

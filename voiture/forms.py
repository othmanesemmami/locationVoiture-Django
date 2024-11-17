# cars/forms.py
from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['matricule', 'marque', 'kilometrage', 'prixjours', 'disponibilite']

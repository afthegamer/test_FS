from django.contrib import admin
from .models import EnergyData

# Enregistrer le modèle EnergyData dans l'interface d'administration
admin.site.register(EnergyData)

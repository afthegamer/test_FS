from django.db import models

class EnergyData(models.Model):
    date = models.DateField()
    region = models.CharField(max_length=100)
    consumption_twh = models.FloatField()

    class Meta:
        verbose_name = "Donnée Énergétique"
        verbose_name_plural = "Données Énergétiques"
        ordering = ['-date', 'region']  # Sort by descending date, then by region

    def __str__(self):
        return f"{self.date} - {self.region} : {self.consumption_twh:.2f} TWh"

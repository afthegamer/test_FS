from ..models import EnergyData

def create_energy_data(date, region, consumption_twh):
    """Crée une entrée de données énergétiques."""
    return EnergyData.objects.create(
        date=date.date(),
        region=region,
        consumption_twh=consumption_twh
    )

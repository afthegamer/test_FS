from django.shortcuts import render
from django.db.models import Sum
from ..models import EnergyData
import json

#View for viewing consumption graphs
def energy_charts(request):
    region_data = EnergyData.objects.values('region').annotate(total_consumption=Sum('consumption_twh'))
    regions = [entry['region'] for entry in region_data]
    consumptions = [entry['total_consumption'] for entry in region_data]

    year_data = EnergyData.objects.values('date__year').annotate(total_consumption=Sum('consumption_twh')).order_by('date__year')
    years = [entry['date__year'] for entry in year_data]
    annual_consumptions = [entry['total_consumption'] for entry in year_data]

    return render(request, 'energy_dashboard/energy_charts.html', {
        'regions': json.dumps(regions),
        'consumptions': json.dumps(consumptions),
        'years': json.dumps(years),
        'annualConsumptions': json.dumps(annual_consumptions),
    })

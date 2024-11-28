from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from ..models import EnergyData
from ..serializers import EnergyDataSerializer

# API to retrieve and create energy data
class EnergyDataListAPI(generics.ListCreateAPIView):
    queryset = EnergyData.objects.all()
    serializer_class = EnergyDataSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# API to retrieve, update or delete energy data
class EnergyDataDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnergyData.objects.all()
    serializer_class = EnergyDataSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Simple API view to retrieve consumption data by year (for AJAX)
def energy_data_api(request):
    year_data = EnergyData.objects.values('date__year').annotate(total_consumption=Sum('consumption_twh')).order_by('date__year')
    data = {
        "years": [entry['date__year'] for entry in year_data],
        "annualConsumptions": [entry['total_consumption'] for entry in year_data],
    }
    return JsonResponse(data)

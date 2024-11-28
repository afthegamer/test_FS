from django.urls import path
from .views.csv_views import upload_csv
from .views.chart_views import energy_charts
from .views.api_views import EnergyDataListAPI, EnergyDataDetailAPI

urlpatterns = [
    path('upload/', upload_csv, name='upload_csv'),  # Route for CSV import
    path('charts/', energy_charts, name='energy_charts'),  # Route to display charts
    path('api/energy-data/', EnergyDataListAPI.as_view(), name='energy_data_api'),  # API view to list/create energy data
    path('api/energy-data/<int:pk>/', EnergyDataDetailAPI.as_view(), name='energy_data_detail_api'),  # API view to retrieve, update or delete specific energy data
]

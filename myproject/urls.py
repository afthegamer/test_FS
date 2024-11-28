from django.contrib import admin
from django.urls import path, include
from energy_dashboard.views.home_view import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home page
    path('energy/', include('energy_dashboard.urls')),  # Inclusion of URLs of the `energy_dashboard application`
]


from django.shortcuts import render

# View for home page
def home(request):
    return render(request, 'energy_dashboard/home.html')

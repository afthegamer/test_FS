import csv
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from energy_dashboard.models import EnergyData
from energy_dashboard.forms import CSVUploadForm


# View for importing CSV data
def upload_csv(request):
    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            decoded_file = csv_file.read().decode('utf-8-sig').splitlines()
            reader = csv.DictReader(decoded_file, delimiter=';')

            rows_to_insert = []
            rows_inserted = 0
            errors = 0

            for row in reader:
                try:
                    if 'Date' not in row or 'Region' not in row or 'Valeur (TWh)' not in row:
                        errors += 1
                        continue

                    value = float(row['Valeur (TWh)'].replace(',', '.'))
                    date_str = row['Date']
                    date_obj = datetime.strptime(date_str, "%Y").replace(month=1, day=1)

                    rows_to_insert.append(EnergyData(
                        date=date_obj.date(),
                        region=row['Region'],
                        consumption_twh=value
                    ))
                    rows_inserted += 1
                except (ValueError, KeyError) as e:
                    errors += 1
                    continue

            # Use bulk_create to insert rows at once
            
            EnergyData.objects.bulk_create(rows_to_insert)

            messages.success(request,
                             f"{rows_inserted} lignes ont été importées avec succès. {errors} erreurs ont été rencontrées.")
    else:
        form = CSVUploadForm()

    data_list = EnergyData.objects.all()
    paginator = Paginator(data_list, 10)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    return render(request, 'energy_dashboard/upload_csv.html', {'form': form, 'page_obj': page_obj})

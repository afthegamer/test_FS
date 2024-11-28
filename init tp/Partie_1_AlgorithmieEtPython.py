import csv
from typing import Dict, Any


def find_peak_consumption(file_path: str) -> Dict[str, Any]:
    with open(file_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        # Initializing peak values
        max_value = -float('inf')
        date = ""
        region = ""


        # Browse data
        for row in reader:
            try:
                value = float(row['Valeur (TWh)'].replace(',', '.'))
            except ValueError:
                # Ignore invalid rows
                continue

            # Update peak if current value is larger
            if value > max_value:
                max_value = value
                date = row['Date']
                region = row['Region']

    # Returns information about the peak found
    return {
        "date": date,
        "region": region,
        "value": max_value
    }



data = find_peak_consumption('elecConso.csv')

# Displaying the result
print(f"La valeur maximale trouvée en TWh est de : {data['value']} en {data['date']} dans la région : {data['region']}")

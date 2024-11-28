import csv
from typing import List

def custom_sort_per_line(file_path: str) -> List[str]:

    # Read CSV file
    with open(file_path, newline='', encoding='utf-8-sig') as csvfile:
        # Skip the first descriptive line
        next(csvfile)

        reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')

        # Clean up column names by removing leading and trailing spaces
        reader.fieldnames = [name.strip() if name else name for name in reader.fieldnames]

        # Check if the expected column is present
        if 'Typologie des données impactées' not in reader.fieldnames:
            raise KeyError(
                f"Colonne 'Typologie des données impactées' non trouvée. En-têtes disponibles : {reader.fieldnames}")

        # Treat each line separately and sort the typologies
        for index, row in enumerate(reader, start=1):  # Use enumerate to have index and row
            if row:
                # Extract the “Typology of impacted data” column"
                typologie = row.get('Typologie des données impactées')
                if typologie:
                    # List to store typologies for the current row
                    typologies = []
                    current_typology = ""
                    inside_parenthesis = 0

                    for char in typologie:
                        if char == ',' and inside_parenthesis == 0:
                            # If there is a comma outside the parentheses, the typology is considered complete.
                            typologies.append(current_typology.strip())
                            current_typology = ""
                        else:
                            # Accumulate characters for the current typology
                            current_typology += char
                            # Management of parentheses to know if we are in a description or not
                            if char == '(':
                                inside_parenthesis += 1
                            elif char == ')':
                                inside_parenthesis -= 1

                    # Add the last typology if it exists
                    if current_typology.strip():
                        typologies.append(current_typology.strip())

                    # Sort the typologies by length then in alphabetical order
                    typologies.sort(key=lambda x: (len(x), x))

                    # Print the sorted typologies for this line
                    print(f"Typologies triées pour la ligne {index} :")
                    for typology in typologies:
                        print(typology)
                    print()  # Empty line to separate lines

# Example of use with CSV file
try:
    custom_sort_per_line('cnilViolation.csv')
except KeyError as e:
    print(e)

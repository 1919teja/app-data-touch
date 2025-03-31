import csv
import random

def generate_touch_data(num_rows, filename="touch_data.csv"):
    """
    Generates synthetic touch area, pressure, and age group data
    and saves it to a CSV file.

    Args:
        num_rows (int): The number of data rows to generate.
        filename (str): The name of the CSV file to save the data to.
    """
    header = ['Touch Area (mm²)', 'Pressure (force)', 'Age Group']
    data = []

    for _ in range(num_rows):
        # Decide the age group first (roughly equal distribution)
        # You could adjust this logic if you want a different distribution
        age_group_choice = random.choice(['Child', 'Teen', 'Adult'])

        if age_group_choice == 'Child':
            # Define ranges for Child
            area = random.randint(70, 140)
            # Pressure generally lower, related to area but with variation
            base_pressure = area / 200.0
            pressure = round(random.uniform(base_pressure * 0.85, base_pressure * 1.15), 2)
            # Clamp pressure to reasonable min/max for the group
            pressure = max(0.35, min(pressure, 0.75))
            age_group = 'Child'

        elif age_group_choice == 'Teen':
            # Define ranges for Teen
            area = random.randint(230, 330)
             # Pressure in mid-range
            base_pressure = area / 200.0
            pressure = round(random.uniform(base_pressure * 0.9, base_pressure * 1.1), 2)
             # Clamp pressure
            pressure = max(1.10, min(pressure, 1.75))
            age_group = 'Teen'

        else: # Adult
            # Define ranges for Adult
            area = random.randint(450, 650)
             # Pressure higher
            base_pressure = area / 200.0
            pressure = round(random.uniform(base_pressure * 0.95, base_pressure * 1.05), 2)
             # Clamp pressure
            pressure = max(2.20, min(pressure, 3.30))
            age_group = 'Adult'

        data.append([area, pressure, age_group])

    # Write data to CSV file
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header) # Write the header row
            writer.writerows(data)  # Write all the data rows
        print(f"Successfully generated {num_rows} rows and saved to '{filename}'")
    except IOError:
        print(f"Error: Could not write to file '{filename}'. Check permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- How to Use ---
# 1. Change the number_of_rows to how many data points you want (e.g., 1000, 2000).
# 2. Change the output_filename if you want a different name for your CSV file.
# 3. Run this Python script. It will create the CSV file in the same directory.

number_of_rows = 1000000  # <--- Set desired number of rows here
output_filename = 'custom_touch_data_1000.csv' # <--- Set desired filename here

generate_touch_data(number_of_rows, output_filename)

# Example for 2000 rows:
# number_of_rows_2k = 2000
# output_filename_2k = 'custom_touch_data_2000.csv'
# generate_touch_data(number_of_rows_2k, output_filename_2k)

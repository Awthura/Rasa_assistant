import csv
import json
import os

# Define the path to the directory containing the CSV file
directory = 'data'

# Define the name of the CSV file
csv_file = 'data.csv'

# Define the name of the JSON file
json_file = 'names.json'

# Open the CSV file and read the contents
with open(os.path.join(directory, csv_file), 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]
# Extract the 'names' from the data
names = [row['Title'] for row in data]

# Convert the names to a JSON file
with open(os.path.join(directory, json_file), 'w') as file:
    json.dump(names, file)
import csv
import json

def read_csv_file(filename):
    data_dict = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Get the headers
        for header in headers:
            data_dict[header] = []  # Initialize an empty list for each header
        for row in reader:
            for index, value in enumerate(row):
                if headers[index] == 'number- not needed':
                    continue  # Skip 'number- not needed' column
                elif headers[index] in ['Academic Skills', 'Fitness Interests']:
                    # Split the comma-separated values and create a list
                    skills_list = value.split(', ')
                    data_dict[headers[index]].append(skills_list)
                else:
                    data_dict[headers[index]].append(value)  # Append value as usual
    return data_dict

data_dict = read_csv_file('UnityUDatabase.csv')

# Convert data_dict to JSON format
data_json = json.dumps(data_dict)

# Write data_json to a JavaScript file
with open('data.js', 'w') as js_file:
    js_file.write(f'var data = {data_json};')

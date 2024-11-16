import pandas as pd
import json
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Convert an Excel file to JSON format.')
parser.add_argument('--input', '-i', required=True, help='Path to the input Excel file')
parser.add_argument('--output', '-o', required=True, help='Path to the output JSON file')

args = parser.parse_args()

# Load the Excel file
df = pd.read_excel(args.input)

# Convert the DataFrame to JSON
json_data = df.to_json(orient='records')

# Save the JSON data to a file
with open(args.output, 'w') as json_file:
    json_file.write(json_data)

print(f"Conversion complete. JSON file saved as '{args.output}'.")
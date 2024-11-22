import pandas as pd
import json
import argparse
import os
import re

# Set up argument parser
parser = argparse.ArgumentParser(description='Convert an Excel file to JSON format.')
parser.add_argument('--input', '-i', required=True, help='Path to the input Excel file')
parser.add_argument('--output', '-o', required=True, help='Path to the output JSON file or folder')
parser.add_argument('--split', '-s', action='store_true', help='Split JSON items into individual files in the output folder')

args = parser.parse_args()

# Load the Excel file
df = pd.read_excel(args.input)

if args.split:
    # Ensure the output directory exists
    os.makedirs(args.output, exist_ok=True)

    # Convert each row to a JSON object and save to individual files
    for idx, row in df.iterrows():
        json_data = row.to_json()
        title = row['title']
        # Replace invalid filename characters with underscore
        valid_title = re.sub(r'[.<>:"/\\|?*]', '_', title)
        output_file = os.path.join(args.output, f'{valid_title}.json')
        with open(output_file, 'w') as json_file:
            json_file.write(json_data)
    print(f"Conversion complete. JSON files saved in folder '{args.output}'.")
else:
    # Convert the DataFrame to JSON
    json_data = df.to_json(orient='records')

    # Save the JSON data to a single file
    with open(args.output, 'w') as json_file:
        json_file.write(json_data)
    print(f"Conversion complete. JSON file saved as '{args.output}'.")
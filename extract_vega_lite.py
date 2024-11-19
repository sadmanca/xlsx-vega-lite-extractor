import pandas as pd
import argparse
from bs4 import BeautifulSoup
import os
import glob

def extract_columns(input_filepath, output_filepath, filename):
    columns_to_extract = [
        "id",
        "title",
        "content",
        "moduleid",
        "lesson_title",
        "lesson_directory",
        "sectionid",
        "section_name",
        "section_directory",
        "section_number",
        "lesson_number",
        "page_number",
    ]

    df = pd.read_excel(input_filepath)

    # Extract the specified columns
    extracted_df = df.loc[:, columns_to_extract]

    # Extract content within the specified HTML tags
    def extract_html_content(html):
        if pd.isna(html):
            return []
        soup = BeautifulSoup(html, 'html.parser')
        pre_tags = soup.find_all('pre', {'id': 'vega-lite-spec', 'class': 'vega-lite'})
        return [pre_tag.get_text().strip() for pre_tag in pre_tags]

    # Apply the extraction function and explode the list into separate rows
    extracted_df['content'] = extracted_df['content'].apply(extract_html_content)
    exploded_df = extracted_df.explode('content')

    # Filter out rows where the content column is empty or contains only whitespace
    filtered_df = exploded_df[exploded_df['content'].apply(lambda x: isinstance(x, str) and x.strip() != '')]

    # Add filename column
    filtered_df['filename'] = filename

    return filtered_df

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract specific columns from an Excel file or all Excel files in a folder."
    )
    parser.add_argument("--input", "-i", required=True, help="Input Excel file path or folder path")
    parser.add_argument("--output", "-o", required=True, help="Output Excel file path")

    args = parser.parse_args()

    if os.path.isdir(args.input):
        all_files = glob.glob(os.path.join(args.input, "*.xlsx"))
        combined_df = pd.DataFrame()
        for file in all_files:
            filename = os.path.splitext(os.path.basename(file))[0]
            extracted_df = extract_columns(file, args.output, filename)
            combined_df = pd.concat([combined_df, extracted_df], ignore_index=True)
        combined_df.to_excel(args.output, index=False)
    else:
        filename = os.path.splitext(os.path.basename(args.input))[0]
        extracted_df = extract_columns(args.input, args.output, filename)
        extracted_df.to_excel(args.output, index=False)
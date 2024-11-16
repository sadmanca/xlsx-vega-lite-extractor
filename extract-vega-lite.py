import pandas as pd
import argparse
from bs4 import BeautifulSoup

def extract_columns(input_filepath, output_filepath):
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
        soup = BeautifulSoup(html, 'html.parser')
        pre_tag = soup.find('pre', {'id': 'vega-lite-spec', 'class': 'vega-lite'})
        return pre_tag.get_text() if pre_tag else ''

    extracted_df.loc[:, 'content'] = extracted_df['content'].apply(extract_html_content)

    # Filter out rows where the content column contains the specified HTML tag
    filtered_df = extracted_df[extracted_df['content'] != '']

    # Write the filtered columns to a new Excel file
    filtered_df.to_excel(output_filepath, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract specific columns from an Excel file."
    )
    parser.add_argument("--input", "-i", required=True, help="Input Excel file path")
    parser.add_argument("--output", "-o", required=True, help="Output Excel file path")

    args = parser.parse_args()

    extract_columns(args.input, args.output)
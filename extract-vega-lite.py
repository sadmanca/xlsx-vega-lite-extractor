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
        if pd.isna(html):
            return []
        soup = BeautifulSoup(html, 'html.parser')
        pre_tags = soup.find_all('pre', {'id': 'vega-lite-spec', 'class': 'vega-lite'})
        return [pre_tag.get_text() for pre_tag in pre_tags]

    # Apply the extraction function and explode the list into separate rows
    extracted_df['content'] = extracted_df['content'].apply(extract_html_content)
    exploded_df = extracted_df.explode('content')

    # Filter out rows where the content column is empty or contains only '{'
    filtered_df = exploded_df[(exploded_df['content'] != '') & (exploded_df['content'] != '{')]

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
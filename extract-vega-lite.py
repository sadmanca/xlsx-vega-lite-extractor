import pandas as pd
import argparse


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

    extracted_df = df[columns_to_extract]

    extracted_df.to_excel(output_filepath, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract specific columns from an Excel file."
    )
    parser.add_argument("--input", "-i", required=True, help="Input Excel file path")
    parser.add_argument("--output", "-o", required=True, help="Output Excel file path")

    args = parser.parse_args()

    extract_columns(args.input, args.output)

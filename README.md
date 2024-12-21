# xlsx-vega-lite-extractor

This repository contains tools for converting Excel files to JSON format and extracting specific columns from Excel files, including processing Vega-Lite specifications.

## Setup and Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/sadmanca/xlsx-vega-lite-extractor.git
   cd xlsx-vega-lite-extractor
   ```

2. **Create a virtual environment**:
   ```sh
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

4. **Install the required dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Converting Excel to JSON

The script `xlsx_to_json.py` converts an Excel file to JSON format.

**Usage**:
```sh
python xlsx_to_json.py --input <input_excel_file> --output <output_json_file_or_folder> [--split]
```

- `--input`, `-i`: Path to the input Excel file.
- `--output`, `-o`: Path to the output JSON file or folder.
- `--split`, `-s`: Option to split JSON items into individual files in the output folder.

**Example**:
```sh
python xlsx_to_json.py --input data.xlsx --output output_folder --split
```

### Extracting Vega-Lite Specifications

The script `extract_vega_lite.py` extracts specific columns from an Excel file and processes Vega-Lite specifications.

**Usage**:
```sh
python extract_vega_lite.py --input <input_excel_file_or_folder> --output <output_excel_file>
```

- `--input`, `-i`: Input Excel file path or folder path.
- `--output`, `-o`: Output Excel file path.

**Example**:
```sh
python extract_vega_lite.py --input data.xlsx --output output.xlsx
```

## License

This repository is licensed under the MIT License.

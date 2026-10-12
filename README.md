This project builds a modular, configuration-driven command-line data processing pipeline to clean, validate, and transform datasets. Data flows sequentially through the pipeline step by step. First, the system validates input paths and loads files of various formats. Next, it runs structural validation and data type checks. Then, it applies cleaning rules such as duplicate removal and outlier filtering. Finally, it exports the cleaned data and generates a summary report.

The project structure consists of a main 'pipeline.py' entry point and a 'src/' directory with dedicated modules:

* `utils.py` handles logging configuration and path checks.
* `data_loaders.py` parses CSV, JSON, and YAML files.
* `data_validator.py` enforces required columns and numeric integrity.
* `data_processor.py` executes cleaning logic and generates summary statistics.
* `data_output.py` ensures output directories exist and saves the final dataset.

### Example Execution & Output

**Example Command:**
```bash
python pipeline.py --input fixtures/sample_data.csv --output output/clean.csv --config config/config.yaml --verbose

16:54:18 DEBUG    __main__ — Arguments parsed: input = fixtures/sample_data.csv, output = output/clean.csv, config = config/config.yaml
16:54:18 INFO     src.utils — Input file validated: fixtures/sample_data.csv
16:54:18 INFO     src.utils — Input file validated: config/config.yaml
16:54:18 INFO     src.data_loader — Loaded CSV file: fixtures\sample_data.csv (100 rows)
16:54:18 INFO     src.data_loader — Loaded YAML file: config\config.yaml
16:54:18 WARNING  src.data_validator — Invalid numeric value 'not_available' in column 'rating' at row 94
16:54:18 WARNING  src.data_validator — Invalid numeric value 'error' in column 'rating' at row 95
16:54:18 WARNING  src.data_validator — Removed 2 rows with invalid numeric values in ['record_id', 'rating']
16:54:18 DEBUG    src.data_validator — Validation: 100 -> 98 rows
16:54:18 INFO     __main__ — Validation complete: 100 -> 98 rows
16:54:18 DEBUG    src.data_processor — remove_duplicates: removed 2 duplicate row(s)
16:54:18 INFO     __main__ — Processing complete: 98 -> 96 rows
16:54:18 DEBUG    src.data_output — Saved 96 rows to output\clean.csv
16:54:18 INFO     __main__ — Saved cleaned data to output/clean.csv

Cleaning report:
{'rows_before': 98, 'rows_after': 96, 'rows_removed': 2, 'columns_before': 5, 'columns_after': 5, 'columns_removed': 0}
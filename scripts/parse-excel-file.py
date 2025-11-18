"""  parse-excel-file.py

  Open the excel file and sheet specified.
  Save the config information (1st 3 rows) as separate csv files.

"""
import pandas as pd
import sys

# Use sheet configuration from confighelper
from confighelper import files, label, sheet_config

# inputs
SHEET_NAME = sheet_config.sheetname


def validate_mandatory_columns(df, label_config):
    """
    Validate that all mandatory column labels exist in the Excel file.
    Skips any field names that start with "display" as these are generated for website use.

    Args:
        df: pandas DataFrame with Excel data
        label_config: namedtuple containing configured column label names

    Raises:
        SystemExit: If any mandatory columns are missing from the DataFrame
    """
    # Extract all field names (keys) from the label namedtuple,
    # excluding any that start with "display" (these are generated for website use)
    field_names = [name for name in label_config._fields if not name.lower().startswith("display")]
    configured_columns = [getattr(label_config, name) for name in field_names]
    missing_columns = [col for col in configured_columns if col not in df.columns]

    if missing_columns:
        print(
            f"ERROR: The following configured columns are missing from the Excel file: {missing_columns}",
            file=sys.stderr,
        )
        print(
            f"Expected columns: {configured_columns}",
            file=sys.stderr,
        )
        print(
            f"Found columns: {list(df.columns)}",
            file=sys.stderr,
        )
        sys.exit(1)


def drop_unfiltered_columns(df, filter_row_idx):
    """
    Drop all columns from `df` that do not contain a filter marker in the
    specified `filter_row_idx` of the DataFrame (before column names are assigned).

    Criteria: keep columns that contain 'Filter_yes' or 'Filter_no' (case-insensitive).
    Drop columns that are empty or contain any other value.

    Args:
        df: pandas DataFrame with `header=None` (row indices align with sheet rows)
        filter_row_idx: Row index containing filter markers

    Returns:
        The pruned DataFrame with unfiltered columns removed.
    """
    # Extract the filter row from the DataFrame
    filter_row = df.iloc[filter_row_idx].map(lambda x: x.strip() if isinstance(x, str) else x)

    # Determine which column positions to keep
    keep_positions = []
    for pos, val in enumerate(filter_row.tolist()):
        if val is None:
            continue
        sval = str(val).strip()
        if sval == "":
            continue
        if sval.lower() in ("filter_yes", "filter_no"):
            # Keep columns marked with either Filter_yes or Filter_no
            keep_positions.append(pos)

    # If no columns marked for keeping, return df unchanged to avoid empty dataset
    if not keep_positions:
        return df

    # Keep only the columns at the marked positions
    df = df.iloc[:, keep_positions]

    return df


def drop_rows_without_id(df, label_config):
    """
    Drop all rows that do not contain a valid (non-empty, non-whitespace) value
    in the ID column.

    Args:
        df: pandas DataFrame with Excel data
        label_config: namedtuple containing the ID column label

    Returns:
        DataFrame with rows containing empty or whitespace-only ID values removed
    """
    id_column = label_config.id

    if id_column not in df.columns:
        # ID column doesn't exist, return df unchanged
        return df

    # Count rows before filtering
    initial_count = len(df)

    # Drop rows where ID is None, empty string, or only whitespace
    df = df[df[id_column].notna() & (df[id_column].astype(str).str.strip() != "")]

    # Log the number of rows dropped
    dropped_count = initial_count - len(df)
    if dropped_count > 0:
        print(
            f"Dropped {dropped_count} row(s) with empty or whitespace-only ID values"
        )

    return df


pd.set_option('future.no_silent_downcasting', True)

# (a) Read the entire Excel file (no header yet, to process config rows and data rows together)
df_full = pd.read_excel(files.excel_file, sheet_name=SHEET_NAME, header=None, dtype="str")

# Normalise (strip whitespace) from all content
df_full = df_full.map(lambda x: x.strip() if isinstance(x, str) else x)

# (b) Drop unwanted columns based on filter markers
df_full = drop_unfiltered_columns(df_full, sheet_config.filterRowIdx)

# Get column labels from the column header row
col_labels = df_full.iloc[sheet_config.colHeaderRowIdx].tolist()
df_full.columns = col_labels

# (c) Extract and write config files from the first few config rows
filter_data = (
    df_full.iloc[[sheet_config.filterRowIdx]]
    .replace({"Filter_yes": True, "Filter_no": False})
    .to_csv(files.filter_config, index=False)
)
search_data = (
    df_full.iloc[[sheet_config.searchRowIdx]]
    .replace({"Search_yes": True, "Search_no": False})
    .to_csv(files.search_config, index=False)
)
full_display_data = (
    df_full.iloc[[sheet_config.fullDisplayRowIdx]]
    .replace({"FullDisplay_yes": True, "FullDisplay_no": False})
    .to_csv(files.doc_display_config, index=False)
)
multi_option_data = (
    df_full.iloc[[sheet_config.multiOptionRowIdx]]
    .replace({"MultiOption_yes": True, "MultiOption_no": False})
    .to_csv(files.multi_option_config, index=False)
)

# (d) Extract data rows from colHeaderRowIdx onwards, clean, and write to CSV
# Extract data rows starting from the row after the column header row
df_data = df_full.iloc[sheet_config.colHeaderRowIdx + 1:].copy()
df_data.columns = col_labels

# Clean the data: drop rows without valid ID
df_data = drop_rows_without_id(df_data, label)

# Validate that all mandatory column labels exist
validate_mandatory_columns(df_data, label)

# Save the cleaned data records to CSV
df_data.to_csv(files.libindex_csv, index=False, encoding="utf-8")

print(
    "{}\n converted to\n {},\n {},\n {}\n, {}\n and {}".format(
        files.excel_file,
        files.libindex_csv,
        files.filter_config,
        files.search_config,
        files.doc_display_config,
        files.multi_option_config,
    )
)

"""  parse-excel-file.py

  Open the excel file and sheet specified.
  Save the config information (1st 3 rows) as separate csv files.

"""
import pandas as pd

from confighelper import files, label

# inputs
SHEET_NAME = "Repository"

# Save only the Active records in the document library index
# Note: index=False prevents pandas from writing a row index to the CSV.
df = pd.read_excel(files.excel_file, sheet_name=SHEET_NAME, header=4, dtype="str")
# Strip pre and post whitespace from all content
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
# Save the active records to a CSV file
df.to_csv(files.libindex_csv, index=False, encoding="utf-8")


# Extract the config data rows and save them as separate CSV files
col_labels = df.columns  # use column labels from previous load of this file
df = pd.read_excel(
    files.excel_file,
    sheet_name=SHEET_NAME,
    header=None,
)
df.columns = col_labels

filter_data = (
    df.iloc[[0]]
    .replace({"Filter_yes": True, "Filter_no": False})
    .to_csv(files.filter_config, index=False)
)
search_data = (
    df.iloc[[1]]
    .replace({"Search_yes": True, "Search_no": False})
    .to_csv(files.search_config, index=False)
)
full_display_data = (
    df.iloc[[2]]
    .replace({"FullDisplay_yes": True, "FullDisplay_no": False})
    .to_csv(files.doc_display_config, index=False)
)
multi_option_data = (
    df.iloc[[3]]
    .replace({"MultiOption_yes": True, "MultiOption_no": False})
    .to_csv(files.multi_option_config, index=False)
)

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

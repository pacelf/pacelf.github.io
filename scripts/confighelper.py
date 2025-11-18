# config.py
#
# This file contains the configurable items for specific
# digital library source data.
#

import configparser
from collections import namedtuple
from pathlib import Path

config = {}


def load_config():
    config = configparser.ConfigParser()
    config.read("library-config.ini")
    return config


def get_sheet_config(config):
    sheet_config = namedtuple(
        "SheetValues", ["sheetname", "filterRowIdx", "searchRowIdx", "fullDisplayRowIdx", "multiOptionRowIdx", "colHeaderRowIdx"]
    )
    return sheet_config(
        sheetname = config["Excel-sheet-format"]["sheetname"],
        filterRowIdx= int(config["Excel-sheet-format"]["filterRowIdx"]),
        searchRowIdx= int(config["Excel-sheet-format"]["searchRowIdx"]),
        fullDisplayRowIdx= int(config["Excel-sheet-format"]["fullDisplayRowIdx"]),
        multiOptionRowIdx= int(config["Excel-sheet-format"]["multiOptionRowIdx"]),
        colHeaderRowIdx= int(config["Excel-sheet-format"]["colHeaderRowIdx"]),
    )


def get_docs_config(config):
    docs_config = namedtuple("Docs", ["file_pattern", "src_path", "dest_path"])
    return docs_config(
        file_pattern=config["Library-docs"]["filePattern"],
        src_path=Path(config["Library-docs"]["srcPath"]).resolve(),
        dest_path=Path(config["Library-docs"]["destPath"]),
    )


def get_label_config(config):
    label_config = namedtuple(
        "Labels",
        [
            "id",
            "title",
            "year",
            "access",
            "filename",
            "publishedURL",
            "displayURL",
            "displayIcon",
            "status",
        ],
    )
    return label_config(
        id=config["Column-labels"]["id"],
        title=config["Column-labels"].get("title", "Title"),
        year=config["Column-labels"].get("year", "Year"),
        access=config["Column-labels"]["access"],
        filename=config["Column-labels"]["filename"],
        publishedURL=config["Column-labels"]["publishedURL"],
        displayURL=config["Column-labels"]["displayURL"],
        displayIcon=config["Column-labels"]["displayIcon"],
        status=config["Column-labels"]["status"],
    )


def get_access_values(config):
    access_config = namedtuple(
        "AccessValues", ["open", "physical_library", "publisher"]
    )
    return access_config(
        open=config["Access-values"]["open"],
        physical_library=config["Access-values"]["physicalLibrary"],
        publisher=config["Access-values"]["publisher"],
    )


def get_status_values(config):
    status_values = namedtuple("StatusValues", ["active", "deleted"])
    return status_values(
        active=config["Status-values"]["active"],
        deleted=config["Status-values"]["deleted"],
    )


def get_icons(config):
    icons = namedtuple("Icons", ["webpage", "download", "support", "library"])
    return icons(
        webpage=config["Icons"]["webpage"],
        download=config["Icons"]["download"],
        support=config["Icons"]["support"],
        library=config["Icons"]["library"],
    )


def get_urls(config):
    urls = namedtuple("URLs", ["physical_library", "contact_us", "download"])
    return urls(
        physical_library=config["URLs"]["physicalLibrary"],
        contact_us=config["URLs"]["contactUs"],
        download=config["URLs"]["download"],
    )


def get_general_config(config):
    """General misc configuration values."""
    general = namedtuple("General", ["missing_value_token"])
    return general(
        missing_value_token=config["General"]["missing_value_token"]
    )


def get_query_config(config):
    """Read query sort presets from config and return a dict of sortings.

    The config section should contain keys with suffixes `_fields` and `_order`.
    Fields are comma-separated. Orders are comma-separated.
    Example:
      name_asc_fields = Title
      name_asc_order = asc
      year_name_asc_fields = Year,Title
      year_name_asc_order = desc,asc
    """
    query_sortings = {}
    if "Query" not in config:
        return query_sortings

    section = config["Query"]
    # discover unique prefixes (before the last underscore)
    prefixes = set()
    for key in section:
        if key.endswith("_fields"):
            prefixes.add(key[: -len("_fields")])
        if key.endswith("_order"):
            prefixes.add(key[: -len("_order")])

    for prefix in prefixes:
        fields_key = f"{prefix}_fields"
        order_key = f"{prefix}_order"
        fields_val = section.get(fields_key, "").strip()
        order_val = section.get(order_key, "").strip()
        if not fields_val:
            continue
        fields = [f.strip() for f in fields_val.split(",") if f.strip()]
        orders = [o.strip() for o in order_val.split(",") if o.strip()] if order_val else []
        query_sortings[prefix] = {"field": fields, "order": orders}

    return query_sortings


def get_internal_files():
    # these are hard-coded file paths, for internal processing
    # use only; so they don't need to be configurable.
    local_paths = namedtuple(
        "LocalPaths",
        [
            "doc_display_config",
            "search_config",
            "filter_config",
            "query_config",
            "multi_option_config",
            "excel_file",
            "libindex_csv",
            "libindex_json",
        ],
    )
    return local_paths(
        doc_display_config=Path("outputs/doc-display-config.csv").resolve(),
        search_config=Path("outputs/search-config.csv").resolve(),
        filter_config=Path("outputs/filter-config.csv").resolve(),
        query_config=Path("outputs/query-config.json").resolve(),
        multi_option_config=Path("outputs/multi-option-config.csv").resolve(),
        excel_file=Path("inputs/library-index.xlsx").resolve(),
        libindex_csv=Path("outputs/library-index.csv").resolve(),
        libindex_json=Path("outputs/library-index.json").resolve(),
    )


# load config info for use
config = load_config()
sheet_config = get_sheet_config(config)
docs = get_docs_config(config)
label = get_label_config(config)
access_types = get_access_values(config)
status_types = get_status_values(config)
icons = get_icons(config)
urls = get_urls(config)
files = get_internal_files()
general = get_general_config(config)
query = get_query_config(config)

#!/usr/bin/env python3
""" create-library-index.py

    This reads the library-index spreadsheet and generates a
    library-index.json file from the information in the spreadsheet.

    The paths and names of files are all defined in constants at
    the top of the file, as are the column names for the csv file.

    The script requires the structlog library to be installed
    (used for logging).
"""
import pandas as pd
import json
import os
import csv
import re
import logging
import structlog
import argparse
import libhelper
from confighelper import (
    docs,
    label,
    access_types,
    status_types,
    icons,
    urls,
    files,
)

is_dry_run = False


def split_multi_option_values(lib_data):
    # Split the multi-option columns in to lists of strings
    # hopefully this won't break the lib_docs.to_json function

    #   Columns that can contain multi-options, the value of the item is
    #   a string containing 1 or more tokens separated by semi-colons.
    #   Extract the tokens and replace the value with an array of strings
    #   where each string is a token.
    #
    multi_option_fields = get_multioption_fields(log)
    for column in multi_option_fields:
        log.debug(
            "split_multi_option_values: splitting {}\n  orig\n{} \nsplit values{}".format(
                column, lib_data[column], lib_data[column].str.split(";")
            )
        )
        lib_data[column] = (
            lib_data[column]
            .str.split(";")
            .apply(lambda x: [item.strip() for item in x])
        )
        log.debug("split_multi_option_values: lib_data[{}]\n".format(lib_data[column]))

    return lib_data

def set_url_and_icon(log, lib_data):
    # set label.url value for access via a physical library
    lib_data.loc[
        lib_data[label.access] == access_types.physical_library, label.displayURL
    ] = urls.physical_library
    lib_data.loc[
        lib_data[label.access] == access_types.physical_library, label.displayIcon
    ] = icons.library

    # set label.url value for open access documents (can download directly from the library)
    lib_data.loc[lib_data[label.access] == access_types.open, label.displayURL] = (
        urls.download + lib_data[label.filename]
    )
    lib_data.loc[
        lib_data[label.access] == access_types.open, label.displayIcon
    ] = icons.download

    # set label.url value for documents accessed from an external website
    lib_data.loc[
        lib_data[label.access] == access_types.publisher, label.displayURL
    ] = lib_data[label.publishedURL]
    lib_data.loc[
        lib_data[label.access] == access_types.publisher, label.displayIcon
    ] = icons.webpage

    return lib_data

def create_library_index(log, is_dry_run, lib_data):
    log.info("Creating library_index for website, {}".format(files.libindex_json))

    # convert the list of dictionary items to json string format
    json_lib_data = lib_data.to_json(orient="records")
    log.info("Documents in library, final count: {}".format(lib_data.index.size))

    if not is_dry_run:
        # write library-index json file for the website to use
        json_array_output_file = files.libindex_json.open(mode="w", encoding="utf-8")
        json_array_output_file.write(json_lib_data)

        log.info("Wrote JSON file to {}".format(files.libindex_json))

    return lib_data


def get_multioption_fields(log):
    data = pd.read_csv(files.multi_option_config)
    fields = data.columns[data.iloc[0]].to_list()
    log.info("The multi-option fields for libary are: {}".format(fields))
    return fields

def get_searchable_fields(log):
    data = pd.read_csv(files.search_config)
    search_fields = data.columns[data.iloc[0]].to_list()
    log.info("The searchable fields for libary are: {}".format(search_fields))
    return search_fields


def get_filter_list(log):
    data = pd.read_csv(files.filter_config)
    filter_items = data.columns[data.iloc[0]].to_list()
    log.info("The filter fields for library are: {}".format(filter_items))
    return filter_items


def remove_private_details(log, lib_data):
    # Read in the appropriate config file and drop any columns
    # from lib_data that are set to False in the config file

    public_labels = pd.read_csv(files.doc_display_config)
    col_list = public_labels.columns[~public_labels.iloc[0]].to_list()
    lib_data = lib_data.drop(columns=col_list)
    log.info("Dropped {} columns".format(col_list))

    return lib_data


def remove_invalid_access_rows(log, lib_data):
    # Get a list of docs with an invalid access type
    problem_docs = lib_data[
        ~lib_data[label.access].isin(access_types._asdict().values())
    ]

    log.debug("valid access types are {}".format(access_types._asdict().values()))

    # log a warning message for these problem docs
    for index, row in problem_docs.iterrows():
        log.warning(
            "ID {} | Invalid access value, [{}] ".format(index, row[label.access])
        )

    # log.debug("remove_invalid_access_rows: problem_docs\n{}".format(problem_docs))

    # Drop any docs with invalid access values
    lib_data = lib_data.drop(index=problem_docs.index.to_list())
    log.info(
        "Number of docs dropped due invalid access types is {}".format(
            problem_docs.index.size
        )
    )

    return lib_data


def remove_openaccess_nofilename_rows(log, lib_data):
    # Remove all rows where access is open and filename is empty

    # Get the list of files for the library.
    doc_list = os.listdir(docs.dest_path)

    # DEBUG - log the list of files in the library, displaying each file on a separate line
    log.debug("Documents in the library: \n{}".format("\n".join(doc_list)))

    # Get a list of the open access docs that don't have a file in the library
    problem_docs = lib_data[
        (lib_data[label.access] == access_types.open)
        & (~lib_data[label.filename].isin(doc_list))
    ]
    # log a warning message for these problem docs
    for index, doc in problem_docs.iterrows():
        log.warning(
            "ID {} | {} access document file is missing, {}".format(
                index, access_types.open, doc[label.filename]
            )
        )

    # Drop any open access documents that we don't have a copy of the document for
    lib_data = lib_data.drop(index=problem_docs.index.to_list())
    log.info(
        "Number of docs dropped due to access is {} but no file found is {}".format(
            access_types.open, problem_docs.index.size
        )
    )

    return lib_data


def remove_publisheraccess_nourl_rows(log, lib_data):
    # Get a list of the external access docs that don't have a URL in the lib data
    problem_docs = lib_data[
        (lib_data[label.access] == access_types.publisher)
        & (lib_data[label.publishedURL] == "")
    ]
    # log a warning message for these problem docs
    for index, doc in problem_docs.iterrows():
        log.warning(
            "ID {} | Doc with {} access {} value is empty".format(
                index, access_types.publisher, label.publishedURL
            )
        )

    # Drop any open access documents that we don't have a copy of the document for
    lib_data = lib_data.drop(index=problem_docs.index.to_list())
    log.info(
        "Number of docs dropped due to being {} but having no URL is {}".format(
            access_types.publisher, problem_docs.index.size
        )
    )
    return lib_data


def remove_nonactive_rows(log, lib_data):
    # Drop all rows that don't have status set to Active
    # unless there is no Status column
    initial_num_docs = lib_data.index.size
    if label.status in lib_data.columns:
        lib_data = lib_data[lib_data.Status == status_types.active]
        log.info("Extracted only the {} records to process".format(status_types.active))

    log.info(
        "Number of docs dropped due to Status not set to {} is {}".format(
            status_types.active, initial_num_docs - lib_data.index.size
        )
    )

    return lib_data


def create_query_config(log, lib_data, search_fields, filter_fields, multi_option_fields):
    # TODO Sorting config is still hard-coded, need to fix this at some point
    log.debug("about to start create_query_config function")
    log.info("Search fields {}".format(search_fields))
    log.info("Filter fields {}".format(filter_fields))
    log.info("Multi-option fields {}".format(multi_option_fields))

    # build aggregations structure as a Dictionary
    filters = {}
    for field in filter_fields:
        if field not in lib_data.columns:
            continue  # skip on to the next filter field

        log.debug(
            "create_query_config: field {}. Is this a multi-option field? {}".format(
                field, field in multi_option_fields
            )
        )
        if field in multi_option_fields:
            unique_filters = set(x for sublist in lib_data[field] for x in sublist)
        else:
            unique_filters = lib_data[field].unique().tolist()

        log.debug(
            "create_query_string: field {},  unique_filters: {}".format(
                field, unique_filters
            )
        )
        filters[field] = {"title": field, "size": len(unique_filters)}
        # log.debug(
        #     "create_query_string: filters[{}]: {}".format(field, filters[field])
        # )

    query_config = {
        "sortings": {
            "name_asc": {
                "field": "Title",
                "order": "asc",
            },
            "year_name_asc": {
                "field": ["Year", "Title"],
                "order": ["desc", "asc"],
            },
        },
        "searchableFields": search_fields,
        "aggregations": filters,
    }

    log.debug("create_query_config: query_config({})".format(query_config))

    # Create/overwrite query_config json file
    # See confighelper.py for file names
    config_file = files.query_config.write_text(
        json.dumps(query_config), encoding="utf-8"
    )

    log.info("Query config into written to {}".format(files.query_config))


if __name__ == "__main__":
    # Specify level of entries to log
    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    )
    log = structlog.get_logger()

    # create parser
    parser = argparse.ArgumentParser()

    # add arguments to the parser
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="don't make any changes but give me some stats on what would happen",
    )

    # parse the command line arguments
    args = parser.parse_args()
    is_dry_run = args.dry_run
    if is_dry_run:
        log.info("This is a dry-run, no changes will be made")

    log.info("Loading csv file from {}.".format(files.libindex_csv))

    # Read in data from the library-index.csv file and ensure that
    # there are no leading or trailing spaces on the contents
    lib_data = pd.read_csv(
        files.libindex_csv, dtype="str", skipinitialspace=True
    ).fillna("NO VALUE")
    log.info("Initial # rows loaded: {}".format(lib_data.index.size))

    lib_data = remove_nonactive_rows(log, lib_data)
    lib_data = remove_invalid_access_rows(log, lib_data)
    lib_data = remove_openaccess_nofilename_rows(log, lib_data)
    lib_data = remove_publisheraccess_nourl_rows(log, lib_data)
    lib_data = split_multi_option_values(lib_data)
    lib_data = set_url_and_icon(log, lib_data)
    # must call remove_nonactive_rows last in case it removes a
    # column needed for other processing
    lib_data = remove_private_details(log, lib_data)

    lib_data = create_library_index(log, is_dry_run, lib_data)
    create_query_config(log, lib_data, get_searchable_fields(log), get_filter_list(log), get_multioption_fields(log))

    log.info("library index and query config file creation is complete")

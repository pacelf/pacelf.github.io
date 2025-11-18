#!/usr/bin/env python3
""" get-library-docs.py

    This reads the library-index.csv file and looks for the
    files listed in the SOURCE_PATH.

    If the ACCESS_RIGHTS type is Open then
    the file is copied into DESTINATION_PATH.

    The paths and names of files are all defined in constants at
    the top of the script, as are the column names for the csv file.

    The script requires the structlog library to be installed
    (used for logging).
"""
import os
import shutil
import csv
import logging
import structlog
import argparse
from confighelper import files, docs, label, status_types, access_types
import libhelper
import unicodedata
import pandas as pd


UNICODE_FORM = "NFKD"


def get_filename_path_dict(log, src_path, pattern):
    # Allows for the src_path to have subdirectories and
    # recursively makes a list of the docs and their paths
    #
    file_list = {}
    for file_path in src_path.glob(pattern):
        if file_path.name != ".DS_Store":
            file_list[unicodedata.normalize(UNICODE_FORM, file_path.name)] = file_path
            log.debug(
                "get_filename_path_dict: file_path.name({}), file_path({})".format(
                    file_path.name, file_path
                )
            )

    log.debug("get_filename_path_dict: filename list: {}".format(file_list.keys()))
    return file_list


if __name__ == "__main__":
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

    # log some useful information
    log.info("Copying files from {}".format(docs.src_path))
    log.info("Copying files to {}".format(docs.dest_path))

    src_file_list = get_filename_path_dict(log, docs.src_path, docs.file_pattern)
    if src_file_list:
      log.debug("Finished building filename and path dictionary")
    else:
        log.error("No source library documents found in {}, exiting now.".format(docs.src_path))
        exit(1)

    # setup some counters for stats at the end
    num_empty_filenames = 0
    num_missing_files = 0
    num_files_in_dest = 0
    num_copied_files = 0

    dest_file_list = os.listdir(docs.dest_path)
    try:
        dest_file_list.remove("Thumbs.db")  # just in case the folder is on Windows
        dest_file_list.remove(".DS_Store")  # just in case the folder is on a Mac
    except ValueError:
        pass

    # log.debug("dest_file_list ({})".format(dest_file_list))
    log.info("#files in {} is {}".format(docs.src_path, len(src_file_list)))
    log.info("#files in {} is {}".format(docs.dest_path, len(dest_file_list)))

    with open(files.libindex_csv, encoding="utf-8") as fd:
        for row in csv.DictReader(fd):
            # strip the trailing whitespace from each row value
            for key, value in row.items():
                row[key] = value.rstrip()

            log.debug(
                "row[{}]({})  access_types.open({}) status_type.active({})  row[{}]({})".format(
                    label.access,
                    row[label.access].lower(),
                    access_types.open,
                    status_types.active,
                    label.status,
                    row[label.status].lower(),
                )
            )
            if (row[label.access].lower() == access_types.open.lower()) and (
                status_types.active == ""
                or (row[label.status].lower() == status_types.active.lower())
            ):
                # get source file name
                src_filename = row[label.filename]

                if src_filename == "":
                    log.warning(
                        "ID {} | {} is {} | {} field is empty".format(
                            row[label.id],
                            label.access,
                            access_types.open,
                            label.filename,
                        )
                    )
                    num_empty_filenames += 1
                    continue  # no filename to work with so log it and move on

                try:
                    log.debug("recorded_pdf_filename: {}".format(src_filename))
                    log.debug("source_file_list {}".format(src_file_list))
                    src_filepath = src_file_list[
                        unicodedata.normalize(UNICODE_FORM, src_filename)
                    ]
                except:
                    log.warning(
                        "ID {} | File {} listed in spreadsheet but not found in {}".format(
                            row[label.id], src_filename, docs.src_path
                        )
                    )
                    num_missing_files += 1
                    continue  # no file to copy, log it and move on

                # replace troublesome characters to create destination file name
                normalised_filename = libhelper.get_normalised_filename(
                    row[label.filename]
                )

                # if the file doesn't already exist in the destination folder
                #  then copy it in. Exit the script if there is an error.
                if normalised_filename not in dest_file_list:
                    try:
                        dest_path = docs.dest_path.joinpath(normalised_filename)
                        if not is_dry_run:
                            shutil.copyfile(src_filepath, dest_path)
                        log.info("Copied {} to {}.".format(src_filepath, dest_path))
                        num_copied_files += 1
                    except Exception as ex:
                        log.exception(
                            "ID {} | copy of {} failed.".format(
                                row[label.id], src_filepath
                            )
                        )
                        exit(1)
                else:
                    log.info(
                        "ID {} | file already exists at destination".format(
                            row[label.id]
                        )
                    )
                    num_files_in_dest += 1

    # Normalise all the filenames in the labels.filename column of the library index
    lib_data = pd.read_csv(files.libindex_csv, dtype="str", skipinitialspace=True).fillna("NO VALUE")
    lib_data[label.filename] = lib_data[label.filename].map(libhelper.get_normalised_filename)
    lib_data.to_csv(files.libindex_csv, index=False, encoding="utf-8")

    log.info(
        "Files copied {} | Files with empty filename {} | File already in dest {} | Missing files {}".format(
            num_copied_files, num_empty_filenames, num_files_in_dest, num_missing_files
        )
    )

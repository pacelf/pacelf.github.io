#!/usr/bin/env python3
''' get-pacelf-files

    This reads the pacelf-index.csv file and looks for the 
    files listed in the SOURCE_PATH.

    If the ACCESS_RIGHTS type is Open then 
    the file is copied into DESTINATION_PATH.

    The paths and names of files are all defined in constants at
    the top of the script, as are the column names for the csv file.

    The script requires the structlog library to be installed
    (used for logging).
'''
import os
from glob import glob
import shutil
from pathlib import Path
import csv
import structlog
import argparse

FILE_PATTERN = "**/*"
SOURCE_PATH = Path("/Volumes/PHTM_PacELF/b PacELF Documents").resolve()
DESTINATION_PATH = Path("./src/statics/data/").resolve()
PACELF_INDEX_FILENAME = "./pacelf-index.csv"

# PacELF index csv file column names
ACCESS_RIGHTS = "Access_Rights"
PDF_FILE_NAME = "PDF_file_name"
ID = "ID"
MANGLED_ID = "\ufeffID"

def get_file_name_path_dict(file_path, pattern):
    file_list = {}
    for file_path in file_path.glob(pattern):
        file_list[file_path.name] = file_path
    
    return file_list

if __name__ == "__main__":
    log = structlog.get_logger()
    # log.setLevel(logging.DEBUG)

    # create parser
    parser = argparse.ArgumentParser()
    
    # add arguments to the parser
    parser.add_argument("--dry-run", action="store_true", help="don't make any changes but give me some stats on what would happen")
    
    # parse the command line arguments
    args = parser.parse_args()
    is_dry_run = args.dry_run
    if is_dry_run: 
        log.info("This is a dry-run, no changes will be made")

    # log some useful information
    log.info("Copying files from {}".format(SOURCE_PATH))
    log.info("Copying files to {}".format(DESTINATION_PATH))

    source_file_list = get_file_name_path_dict(SOURCE_PATH, FILE_PATTERN)
    log.info("Finished building filename and path dictionary")

    # setup some counters for stats at the end
    num_empty_filenames = 0
    num_missing_files = 0
    num_files_in_dest = 0
    num_copied_files = 0

    destination_file_list = os.listdir(DESTINATION_PATH)

    log.info("#files in {} is {}".format(SOURCE_PATH, len(source_file_list)))
    log.info("#files in {} is {}".format(DESTINATION_PATH, len(destination_file_list)))

    with open(PACELF_INDEX_FILENAME, encoding='utf-8') as fd:

        os.chdir(DESTINATION_PATH)  
        log.info("Current working directory is {} ".format(os.getcwd()))      

        for row in csv.DictReader(fd):
            row[ID] = row.pop(MANGLED_ID)   # deal with the initial unicode char that indicates that this is a UTF-8 file

            # strip the trailing whitespace from each row value
            for key, value in row.items():
                row[key] = value.rstrip()

            if row[ACCESS_RIGHTS].lower() == "open":

                # get source file name
                recorded_pdf_name = row[PDF_FILE_NAME]

                if recorded_pdf_name == "":
                    log.warning("ID {} | {} is Open | {} field is empty".format(row[ID], ACCESS_RIGHTS, PDF_FILE_NAME))
                    num_empty_filenames += 1
                    continue    # no filename to work with so log it and move on

                try:
                    recorded_pdf_path = source_file_list[recorded_pdf_name]
                except:
                    log.warning("ID {} | File {} listed in spreadsheet but not found in {}".format(row[ID], recorded_pdf_name, SOURCE_PATH))
                    num_missing_files += 1
                    continue    # no file to copy, log it and move on

                # replace troublesome characters to create destination file name
                normalised_pdf_file_name = row[PDF_FILE_NAME].replace(" ", "_").replace("/", "_")

                # if the file doesn't already exist in the destination folder
                #  then copy it in. Exit the script if there is an error. 
                if normalised_pdf_file_name not in destination_file_list:
                    try:
                        destination_pdf_path = DESTINATION_PATH.joinpath(normalised_pdf_file_name)
                        if not is_dry_run:
                            shutil.copyfile(recorded_pdf_path, destination_pdf_path)
                        log.info("Copied {} to {}.".format(recorded_pdf_path, destination_pdf_path))
                        num_copied_files += 1
                    except Exception as ex:
                        log.exception("ID {} | copy of {} failed.".format(row[ID], recorded_pdf_path))
                        exit(1)
                else:
                    log.info("ID {} | file already exists at destination".format(row[ID]))
                    num_files_in_dest += 1

    log.info(
        "Files copied {} | Files with empty PDF filename {} | File already in dest {} | Missing files {}".format(
        num_copied_files, num_empty_filenames, num_files_in_dest, num_missing_files
    ))

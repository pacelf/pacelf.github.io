#!/usr/bin/env python3
''' csv-to-json

    This reads the pacelf-index.csv spreadsheet and generates a 
    pacelf-index.json file from the information in the spreadsheet.

    It also creates files for entries in the csv with 
    Access_Rights == "Contact PacELF at JCU"

    The paths and names of files are all defined in constants at
    the top of the file, as are the column names for the csv file.

    The script requires the structlog library to be installed
    (used for logging).
'''

import json
import os
from pathlib import Path
import csv
import structlog
from fpdf import FPDF
import argparse

# paths and filenames
PACELF_INDEX_FILE = Path("./pacelf-index.csv").resolve()
PACELF_DOCS_PATH = Path("./src/statics/data/").resolve()
JSON_FILENAME = "pacelf-index.json"
JSON_PATH = Path("./src/pages").resolve()

CONTACT_PACELF_AT_JCU_TEXT = "Please email pacelf@jcu.edu.au to request this item, quoting the PacELF ID number {}.\n We will do our best to make it available, by scanning if necessary and redacting any personal identifying information."

# pacelf-index.csv column names used in processing
#
ID = "ID"
MANGLED_ID = "\ufeffID"     # for dealing with the UTF-8 header
ACCESS_RIGHTS = "Access_Rights"
PDF_FILE_NAME = "PDF_file_name"
UPDATED_FILENAME = "Fixed_TXT_file_name"
DOWNLOAD_URL = "download_url"
PUBLISHER_URL = "View_at_Publisher"

# append everything variable
final_json = []
is_dry_run = False

def normalise_file_name(filename):
    return filename.replace(" ", "_").replace("/", "_")

def create_access_notice_PDF(log, file_info, os):
    ''' Write a txt file to the PacELF documents directory and 
    make that the download url
    '''
    
    normalised_txt_file_name = normalise_file_name(
        "{}.pdf".format(file_info[ID]))

    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font("arial", "B", 13.0)
    pdf.multi_cell(
        h=5.0,
        align="L",
        w=0,
        txt=CONTACT_PACELF_AT_JCU_TEXT.format(file_info[ID]),
        border=0,
    )

    if not is_dry_run:
        pdf.output(normalised_txt_file_name, "F")

        if os.path.isfile(normalised_txt_file_name):
            # the download url is served from a different base directory
            # hence the different path
            download_url = "/statics/data/{}".format(normalised_txt_file_name)
            file_info[UPDATED_FILENAME] = normalised_txt_file_name
            file_info[DOWNLOAD_URL] = download_url
            log.info(
                "ID {} | Created 'Contact PacELF at JCU' access notification file, {} with DOWNLOAD_URL {}".format(
                    file_info[ID], normalised_txt_file_name, download_url
                    )
            )
        else:
            log.warning("ID {} | Creation of 'Contact PacELF at JCU' access notification file failed".format(file_info[ID]))
    else:   # dry run so we will just log what we would have done
        log.info("ID {} | Create 'Contact PacELF at JCU' access notification file, {}".format(
                    file_info[ID], normalised_txt_file_name)
        )

    return file_info

def set_publisher_url_as_download_url(log, file_info):
    if file_info[PUBLISHER_URL] == "":
        log.warning("ID {} | Does not contain a {} entry".format(file_info[ID], PUBLISHER_URL))
    else:
        file_info[DOWNLOAD_URL] = file_info[PUBLISHER_URL]
        log.info("ID {} | Set {} to {}".format(file_info[ID], PUBLISHER_URL, file_info[PUBLISHER_URL]))

    return file_info

def check_file_exists(log, file_info, os):
    ''' Check a file exists and normalise its name if necessary.

    If the filename is empty then create a access notificaton
    file as if the Access_Rights == "Contact PacELF at JCU"

    This function should only be called if Access_Rights == "Open",
    so there should be a file for the document.
    Log warnings if there is no file name in the file_info or if the file doesn't exist.
    '''

    # extract existing name and web friendly name
    recorded_pdf_name = file_info[PDF_FILE_NAME]
    normalised_pdf_file_name = normalise_file_name(recorded_pdf_name)

    if file_info[PDF_FILE_NAME] == "":
        # This file doesn't have a PDF file name in the csv file so we will 
        # create an access notice pdf for it.
        log.warning("ID {} | Open access document has no PDF_FILE_NAME in spreadsheet. Created Contact PacELF access notice file.".format(file_info[ID]))
        return create_access_notice_PDF(log, file_info, os)

    # if the original file name still exists, we need to rename it to a convention - in this case, underscores
    if os.path.isfile(recorded_pdf_name) and not os.path.isfile(normalised_pdf_file_name):

        try:
            if not is_dry_run:
                os.rename(recorded_pdf_name, normalised_pdf_file_name)

            log.info("ID {} | Renamed {} to {}.".format(recorded_pdf_name, normalised_pdf_file_name))
        except Exception as ex:
            log.exception("ID {} | Rename of {} failed.".format(file_info["ID"], recorded_pdf_name))

    if is_dry_run:
        if not (os.path.isfile(recorded_pdf_name) or os.path.isfile(normalised_pdf_file_name)):
            log.warning("ID {} | Open access document does not exist.".format(file_info[ID]))
        else:
            log.info("ID {} | Document exists and will be added to JSON file".format(file_info[ID]))
            
        return file_info

    # check if a file with the normalised name exists before setting download_url to the underscored file name
    if os.path.isfile(normalised_pdf_file_name):

        # the download url is served from a different base directory
        # hence the different path
        download_url = "/statics/data/{}".format(normalised_pdf_file_name)

        file_info[UPDATED_FILENAME] = normalised_pdf_file_name
        file_info[DOWNLOAD_URL] = download_url

        log.info(
            "ID {} | Setting download_url to {}".format(file_info[ID], file_info[DOWNLOAD_URL])
        )
    else:
        log.warning("ID {} | Open access document does not exist.".format(file_info[ID]))

    return file_info


if __name__ == "__main__":

    log = structlog.get_logger()

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
    log.info("Creating/renaming files in {}".format(PACELF_DOCS_PATH))
    log.info("Loading csv file from {}".format(PACELF_INDEX_FILE))

    with open(PACELF_INDEX_FILE, encoding='utf-8') as fd:
        # change cwd to the directory which contains data files
        os.chdir(PACELF_DOCS_PATH)

        for row in csv.DictReader(fd):
            file_info = ""

            row[ID] = row.pop(MANGLED_ID)

            # strip the trailing whitespace from each row value
            for key, value in row.items():
                row[key] = value.rstrip()

            # we do all our processing based on the access rights value for the document
            if "Contact" in row[ACCESS_RIGHTS]:
               file_info = create_access_notice_PDF(log, row, os)
            elif "Open via Publisher" == row[ACCESS_RIGHTS]:
                file_info = set_publisher_url_as_download_url(log, row)
            elif "open" == row[ACCESS_RIGHTS].lower():
                row[ACCESS_RIGHTS] = 'Open' # ensure correct case
                file_info = check_file_exists(log, row, os)
            else:
                log.warning("ID {} | Invalid Access_Rights field value '{}'".format(row[ID], row[ACCESS_RIGHTS]))

            final_json.append(file_info)

    output = json.dumps(final_json)

    # write to file
    os.chdir(JSON_PATH)

    json_array_output_file = open(JSON_FILENAME, "w")
    json_array_output_file.write(output)

    log.info("Wrote JSON file, {}, to {}. Exiting.".format(json_array_output_file, JSON_PATH))

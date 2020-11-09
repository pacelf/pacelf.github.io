#!/usr/bin/env python3
import json
import os
from pathlib import Path
import csv
import structlog
from fpdf import FPDF

# adds a JSON logger for giggles
log = structlog.get_logger()
structlog.configure(processors=[structlog.processors.JSONRenderer()])

# path the input CSV
CSV_FILENAME = "./PacELF_Phase4/modified/Phase_4_added_naming_conventions.csv"

# path to the folder holding the output JSON
OUTPUT_DIRECTORY = "./src/pages/"

CONTACT_PACELF_AT_JCU_TEXT = "Please email pacelf@jcu.edu.au to request this item, quoting the PacELF ID number {}.\n We will do our best to make it available, by scanning if necessary and redacting any personal identifying information."

OPEN_VIA_PUBLISHER_TEXT = "This document may be available to you depending on your personal or institution's subscriptions.  If not, please email pacelf@jcu.edu.au with the PacELF ID for assistance."

# append everything variable
final_json = []

if __name__ == "__main__":

    with open(CSV_FILENAME) as fd:
        # change cwd to the directory which contains data files
        path = "./src/statics/data/"
        os.chdir(path)

        for row in csv.DictReader(fd):
            # pprint(row)

            # various operations on the data before appending to output

            # strip the trailing whitespace from each row value
            for key, value in row.items():
                row[key] = value.rstrip()

            # check the access rights value

            if "Contact" in row["Access_Rights"]:

                # Write a txt file to the data directory and make that the download url
                # TODO: extract this and the rest into a function once done.

                log.msg("Access_Rights is Contact PacELF at JCU.")
                log.msg(
                    "Starting to create placeholder text PDF file for data folder..."
                )

                normalised_txt_file_name = "{}.pdf".format(
                    row["ID"].replace(" ", "_").replace("/", "_")
                )
                log.msg("Using {} for txt file name.".format(normalised_txt_file_name))

                pdf = FPDF()
                pdf.add_page()
                pdf.set_xy(0, 0)
                pdf.set_font("arial", "B", 13.0)
                pdf.multi_cell(
                    h=5.0,
                    align="L",
                    w=0,
                    txt=CONTACT_PACELF_AT_JCU_TEXT.format(row["ID"]),
                    border=0,
                )

                pdf.output(normalised_txt_file_name, "F")

                #  write content to .txt file
                # with open(normalised_txt_file_name, "w") as text_file:
                #     print(
                #         CONTACT_PACELF_AT_JCU_TEXT.format(row["ID"]), file=text_file
                #     )

                if os.path.isfile(normalised_txt_file_name):

                    # the download url is served from a different base directory
                    # hence the different path
                    download_url = "/statics/data/{}".format(normalised_txt_file_name)
                    row["Fixed_TXT_file_name"] = normalised_txt_file_name
                    row["download_url"] = download_url
                    log.msg(
                        "Setting download_url to normalised path : {}".format(
                            row["download_url"]
                        )
                    )

            elif "Publisher" in row["Access_Rights"]:
                log.msg("Access_Rights is Open via Publisher.")
                log.msg("Setting download_url to {}".format(row["View_at_Publisher"]))

                row["download_url"] = row["View_at_Publisher"]

            elif "Open" in row["Access_Rights"]:

                # extract existing name and web friendly name
                recorded_pdf_name = row["PDF_file_name"]
                normalised_pdf_file_name = (
                    row["PDF_file_name"].replace(" ", "_").replace("/", "_")
                )

                # if the original file name still exists, we need to rename it to a convention - in this case, underscores
                if os.path.isfile(recorded_pdf_name):

                    # rename it without any paths with error handling if the file is already renamed
                    try:
                        os.rename(recorded_pdf_name, normalised_pdf_file_name)
                        log.msg(
                            "Renamed {} to {}.".format(
                                recorded_pdf_name, normalised_pdf_file_name
                            )
                        )

                    except FileNotFoundError:
                        print(
                            "File {} does not exist or already renamed.".format(
                                recorded_pdf_name
                            )
                        )

                # check if underscored file name exists before set download_url to the underscored file name

                if os.path.isfile(normalised_pdf_file_name):

                    # the download url is served from a different base directory
                    # hence the different path
                    download_url = "/statics/data/{}".format(normalised_pdf_file_name)

                    row["Fixed_PDF_file_name"] = normalised_pdf_file_name
                    row["download_url"] = download_url

                    log.msg(
                        "Setting download_url to normalised path : {}".format(
                            row["download_url"]
                        )
                    )

            final_json.append(row)

    output = json.dumps(final_json)

    # write to file
    project_dir = Path(__file__).resolve().parent
    os.chdir(project_dir)

    json_array_output_file = open("src/pages/pacelfv4.json", "w")
    json_array_output_file.write(output)

    log.msg("Wrote JSON file: {} to disk. Exiting.".format(json_array_output_file))

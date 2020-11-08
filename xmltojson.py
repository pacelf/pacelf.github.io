#!/usr/bin/env python3
import xmltodict
import json
import os
from pathlib import Path

# path to the folder holding the XML
input_directory = "./src/statics/data/"

# path to the folder holding the output JSON
output_directory = "./src/pages/"

if __name__ == "__main__":

    # while testing clean the output directory first
    # shutil.rmtree("./output/")
    # os.mkdir("./output/")

    final_json = []

    # iterate over the XML files in the folder
    for filename in os.listdir(input_directory):
        if filename.endswith(".xml"):

            filepath = input_directory + filename
            f = open(filepath, encoding="utf-8")

            XML_content = f.read()

            # parse the content of each file using xmltodict
            x = xmltodict.parse(XML_content)

            pacelf_whole_document = x

            # remove the outer XML namespace since not useful
            pacelf_document = pacelf_whole_document["rdsi.pacelf.phase3:document"]

            filename_of_txt = filename.replace(".xml", ".txt")
            filename_of_pdf = filename.replace(".xml", ".pdf")

            path_of_txt = Path(input_directory + filename_of_txt)
            path_of_pdf = Path(input_directory + filename_of_pdf)

            # check if this file exists and if so write it as the download_url
            if path_of_pdf.exists():
                # path exists
                pacelf_document["download_url"] = "/statics/data/" + filename_of_pdf
            else:
                pacelf_document["download_url"] = "/statics/data/" + filename_of_txt

            # other changes to fields

            # renaming volume-issue to more consistent volume_issue
            if "volume-issue" in pacelf_document:
                pacelf_document["volume_issue"] = pacelf_document["volume-issue"]
                del pacelf_document["volume-issue"]
            final_json.append(pacelf_document)

            # print("State of final_json object :")
            # print(final_json)

            # j = json.dumps(pacelf_document)
            #
            #
            # print("Writing" + filename)
            #
            # filename = filename.replace(".xml", "")
            # output_file = open(output_directory + filename + ".json", "w")
            # output_file.write(j)

    output = json.dumps(final_json)

    json_array_output_file = open(output_directory + "pacelf-from-xml" + ".json", "w")
    json_array_output_file.write(output)

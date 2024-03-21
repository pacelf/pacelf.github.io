""" libhelper.py

    Functions needed in more than one script
"""


def get_normalised_filename(filename):
    return filename.replace(" ", "_").replace("/", "_")

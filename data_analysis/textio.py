#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""parse
"""

from __future__ import print_function, unicode_literals

from glob import glob
from os import path
import subprocess

PARSED_PATH = "output.txt"


def pdf_to_text(file_path, parsed_path=PARSED_PATH):

    print("Parsing \'%s\'..." % path.basename(file_path), end=" ")

    subprocess.call(["pdftotext", file_path, parsed_path])

    with open(parsed_path) as parsed_file:
        parsed_text = (
            line.decode("utf-8").strip() for line in parsed_file.readlines()
        )

    print("Done")
    return " ".join(parsed_text)


def lsfile(*data_dir):

    return glob(path.join(*data_dir))


if __name__ == '__main__':

    hard_coded_path = "../data/justin.pdf"
    pdf_to_text(hard_coded_path)

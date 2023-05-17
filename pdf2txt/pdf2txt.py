#!/usr/bin/env python3

import pdftotext

# Load your PDF
convert_this_file = input('What file would you like to convert? ')
with open(convert_this_file, "rb") as f:
    pdf = pdftotext.PDF(f)

# How many pages?
print(len(pdf))

# Read all the text into one string
print("\n\n".join(pdf))

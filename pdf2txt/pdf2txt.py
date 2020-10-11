#!/usr/bin/env python3

import pdftotext

# Load your PDF
with open("lorem_ipsum.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# How many pages?
print(len(pdf))

# Read all the text into one string
print("\n\n".join(pdf))

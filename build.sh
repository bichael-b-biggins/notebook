#!/bin/bash

python3 generate.py
pdflatex notebook.tex

# Generate a second time to get the table of contents working properly.
pdflatex notebook.tex

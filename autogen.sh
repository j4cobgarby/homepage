#!/usr/bin/bash
# Call the jinja code whenever any html file changes
find . -iname "*.html" | entr python3 gen.py
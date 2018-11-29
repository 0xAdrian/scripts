#!/bin/python
# Converter of strings to CharCode JavaScript
# 0xAdrian

import sys

string = sys.argv[1]
JS = "String.fromCharCode("
CHARS = ""
j = 1

for i in string:
        CHARS = CHARS + str(ord(i))
        if j < len(string):
                CHARS = CHARS + ","
        j = j + 1
JS = JS + CHARS + ")"
print JS

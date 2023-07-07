"""
Created by Andreas Oven Aalsaunet
This script takes one or several file names, a wildcard * (representing all files in the current directory)
or a wildcard + file filter (e.g *.py) as argument to output the number of lines, words per selected files in addtion
to their total counts.
"""

import os
import sys

totalLines = 0   # Total number of lines
totalWords = 0   # Total number of words
totalChars = 0   # Total number of characters


def counts():
    """Returns the number of lines, words and character of the filename"""
    global totalLines, totalWords, totalChars
    lines = 0   # Number of lines in file
    words = 0   # Number of words in file
    chars = 0   # Number of characters in file

    with open(filename, 'r') as file:
        content = file.readlines()
        for line in content:
            lines += 1
            words += len(line.split())
            chars += len(line) + 1  # Accounting for the chopped newlines

    totalLines += lines
    totalWords += words
    totalChars += chars
    print(lines, words, chars, filename)


for filename in sys.argv[1:]:
    if os.path.isfile(filename):
        counts()
    else:
        print(filename, "is a directory")

print(totalLines, totalWords, totalChars, "Total")

#!/usr/bin/env python3
"""
Program Name: Template Program
Description: A brief description of what the program does.
Author: Your Name
Date: YYYY-MM-DD
"""

# Import necessary modules

# Global constants and variables
# VERSION = "1.0.0"

import re


def contains_delimeter(text):
    """
    Check if the input text contains ' - ' or ' by ' using regex.

    :param text: A line of text to check.
    :return: True if the text contains ' - ' or ' by ', False otherwise.
    """
    # Define the regex pattern
    pattern = r" - | by "

    # Search for the pattern in the text
    return bool(re.search(pattern, text, re.IGNORECASE))


def main():
    """
    Main function of the program.
    """
    # open raw book file and print contents

    # Specify the file path
    file_path = "books_raw.txt"
    # Open the file in read mode

    with open(file_path, mode="r", encoding="utf-8") as file:
        # Iterate through each line in the file
        for line in file:
            if contains_delimeter(line):
                # Print the line, removing any trailing whitespace
                print("Yes: ", line.strip())
            else:
                print("No:  ", line.strip())


if __name__ == "__main__":
    main()

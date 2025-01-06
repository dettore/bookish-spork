#!/usr/bin/env python3
"""
Program Name: Template Program
Description: A brief description of what the program does.
Author: Your Name
Date: YYYY-MM-DD
"""

# Import necessary modules

# Global constants and variables
#VERSION = "1.0.0"



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
            # Print the line, removing any trailing whitespace
            print(line.strip())


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Program Name: Template Program
Description: A brief description of what the program does.
Author: Your Name
Date: YYYY-MM-DD
"""

import argparse
import logging
# Import necessary modules
import os
import sys

# Global constants and variables
VERSION = "1.0.0"
LOG_FILE = "clean_books.log"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)


def parse_arguments():
    """
    Parse command-line arguments.
    :return: Parsed arguments
    """
    parser = argparse.ArgumentParser(description="Template Program")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {VERSION}")
    parser.add_argument("-o", "--output", type=str, help="Specify output file.")
    return parser.parse_args()


def main():
    """
    Main function of the program.
    """
    # Parse arguments
    args = parse_arguments()

    # Example logic
    if args.output:
        logging.info(f"Output will be saved to {args.output}")
    else:
        logging.info("No output file specified.")

    # Add core logic here
    logging.info("Program execution started.")
    
    # open raw book file and print contents

    # Specify the file path
    file_path = "books_raw.txt"
 
    # Open the file in read mode
    with open(file_path, "r") as file:
        # Iterate through each line in the file
        for line in file:
            # Print the line, removing any trailing whitespace
            print(line.strip())

    logging.info("Program execution finished.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)
        sys.exit(1)

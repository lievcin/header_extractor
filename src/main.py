import argparse
import logging
import os
import sys

from pathlib import Path
from parser import Parser

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    usage = """
    Usage: #TODO
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-if", "--input_file", type=str, required=True)
    parser.add_argument("-of", "--output_file", type=str, required=False)

    args = parser.parse_args()

    if not Path(args.input_file).is_file():
        logger.error("Input file doesn't exist. Please provide valid input.")
        sys.exit(-1)

    parsed = Parser(args.input_file)
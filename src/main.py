import argparse
import logging
import os
import sys

from pathlib import Path
from parsers.regex import RegexParser
from parsers.jaccard import JaccardParser

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    usage = """
    Usage: #TODO
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-if", "--input_file", type=str, required=True)
    parser.add_argument("-of", "--output_file", type=str, required=False)
    parser.add_argument("-p", "--parser", type=str, required=False, default="regex")

    args = parser.parse_args()

    if not Path(args.input_file).is_file():
        logger.error("Input file doesn't exist. Please provide valid input.")
        sys.exit(-1)

    if args.parser=="regex":
        parsed = RegexParser(args.input_file)
    elif args.parser=="jaccard":
        parsed = JaccardParser(args.input_file)
    else:
        logger.error("parser option not recognized, valid options are 'regex' or 'jaccard'")
        sys.exit(-1)

    print("Headers found at indices: {}".format(parsed.headers_indices))
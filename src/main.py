import argparse
import logging
import sys

from pathlib import Path
from parsers.regex import RegexParser
from parsers.jaccard import JaccardParser

logger = logging.getLogger(__name__)

import pprint

pp = pprint.PrettyPrinter(indent=4)

if __name__ == "__main__":
    usage = """
    Usage: This extractor can identify headers in NDA style agreements.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-if",
        "--input_file",
        type=str,
        required=True,
        help="full path to the file to be parsed.",
    )
    parser.add_argument(
        "-p",
        "--parser",
        type=str,
        required=False,
        default="regex",
        help="parsed to use, regex or jaccard.",
    )
    parser.add_argument(
        "-ot",
        "--output_type",
        type=str,
        required=False,
        default="index",
        help="output headers or indices.",
    )

    args = parser.parse_args()

    if not Path(args.input_file).is_file():
        logger.error("Input file doesn't exist. Please provide valid input.")
        sys.exit(-1)

    if args.parser == "regex":
        parsed = RegexParser(args.input_file)
    elif args.parser == "jaccard":
        parsed = JaccardParser(args.input_file)
    else:
        logger.error(
            "parser option not recognized, valid options are 'regex' or 'jaccard'"
        )
        sys.exit(-1)

    if args.output_type == "index":
        print("Headers found at indices:")
        pp.pprint(parsed.headers_indices)
    elif args.output_type == "text":
        print("Headers text found in document:")
        for header in parsed.headers_text:
            pp.pprint(header)
    else:
        logger.error(
            "output format option not recognized, valid options are 'index' or 'text'"
        )
        sys.exit(-1)

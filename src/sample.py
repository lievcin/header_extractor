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
    Usage: This extractor identifies headers in a sample NDA document in the project.
    """

    parser = argparse.ArgumentParser()
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

    SAMPLE_FILE = "reference-files/letter.json"
    if not Path(SAMPLE_FILE).is_file():
        logger.error("Sample file doesn't exist. Cannot run sample, please verify that the project was fully copied.")
        sys.exit(-1)

    if args.parser == "regex":
        parsed = RegexParser(SAMPLE_FILE)
    elif args.parser == "jaccard":
        parsed = JaccardParser(SAMPLE_FILE)
    else:
        logger.error(
            "parser option not recognized, valid options are 'regex' or 'jaccard'"
        )
        sys.exit(-1)

    if args.output_type == "index":
        print("For sample file letter.json, headers found at indices:")
        pp.pprint(parsed.headers_indices)
    elif args.output_type == "text":
        print("For sample file letter.json, headers text found in document:")
        for header in parsed.headers_text:
            pp.pprint(header)
    else:
        logger.error(
            "output format option not recognized, valid options are 'index' or 'text'"
        )
        sys.exit(-1)
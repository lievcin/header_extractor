import logging

logger = logging.getLogger(__name__)

import sys

sys.path.append(".")

from src.config import config
from parsers.base import Parser


import re

HEADER_PATTERNS = "|".join([r["pattern"] for r in config.regex])


class RegexParser(Parser):
    """
    #TODO
    Args:
        path: path to the file file to load
    """

    def __init__(self, path):
        super().__init__(path)

    def _get_headers_text(self):
        headers_text = []
        for item in self.data:
            m = re.match(HEADER_PATTERNS, item["p_text"])
            if m:
                headers_text.append(item["p_text"])
        return headers_text

    def _get_headers_indices(self):
        headers_indices = []
        for item in self.data:
            m = re.match(HEADER_PATTERNS, item["p_text"])
            if m:
                headers_indices.append(item["p_id"])
        return headers_indices

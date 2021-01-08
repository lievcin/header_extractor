import logging
import sys

sys.path.append(".")
logger = logging.getLogger(__name__)

from src.config import config
from parsers.base import Parser
import re


HEADER_PATTERNS = "|".join([r["pattern"] for r in config.regex])


class RegexParser(Parser):
    """
    Parser that uses the regex patters in the config file. It inherits most methods from the parent
    but extracting the indices or text is not inherited.
    """

    def __init__(self, path):
        super().__init__(path)

    def _get_headers_text(self):
        """
        Identifies paragraph text if satisfies a regex pattern.
        """
        headers_text = []
        for item in self.data:
            m = re.match(HEADER_PATTERNS, item["p_text"])
            if m:
                headers_text.append(item["p_text"])
        return headers_text

    def _get_headers_indices(self):
        """
        Identifies paragraph indices if the corresponding text satisfies a regex pattern.
        """
        headers_indices = []
        for item in self.data:
            m = re.match(HEADER_PATTERNS, item["p_text"])
            if m:
                headers_indices.append(item["p_id"])
        return headers_indices

import logging
import sys
sys.path.append(".")

import json
import jsonschema
from src.config import config

logger = logging.getLogger(__name__)

import re
PATTERNS = "|".join([r["pattern"] for r in config.regex])

class Parser(object):
    """
    #TODO
    Args:
        path: path to the file file to load
    """
    def __init__(self, path):
        self.path = path
        self.data = self._validate_json(path)
        self._validate_schema()

    def _validate_json(self, path):
        with open(path) as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError as e:
                logger.error("Input file error: {}".format(e))
                sys.exit(-1)
        return data

    def _validate_schema(self):
        for item in self.data:
            try:
                jsonschema.validate(instance=item, schema=config.schema)
            except jsonschema.exceptions.ValidationError as e:
                logger.error("Input file contains records that don't match the required schema: {}".format(e))

    def _get_headers_text(self):
        headers_text = []
        for item in self.data:
            m = re.match(PATTERNS, item["p_text"])
            if m:
                headers_text.append(item["p_text"])
        return headers_text

    def _get_headers_indices(self):
        headers_indices = []
        for item in self.data:
            m = re.match(PATTERNS, item["p_text"])
            if m:
                headers_indices.append(item["p_id"])
        return headers_indices

    @property
    def headers_text(self):
        return self._get_headers_text()

    @property
    def headers_indices(self):
        return self._get_headers_indices()
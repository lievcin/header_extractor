import logging
import sys

sys.path.append(".")
logger = logging.getLogger(__name__)

from src.config import config
import json
import jsonschema


class Parser(object):
    """
    #Contains methods needed to validate, extract and identify headers given a
    set of paragraphs in JSON format.
    Args:
        path: path to the file file to load
    """

    def __init__(self, path):
        self.path = path
        self.data = self._validate_json(path)
        self._validate_schema()

    def _validate_json(self, path):
        """
        Validates that the file is a valid json object.
        An optional encoding format would be required in order to import files that are not utf-8 encoded. #TODO
        """
        with open(path) as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError as e:
                logger.error("Input file error: {}".format(e))
                sys.exit(-1)
        return data

    def _validate_schema(self):
        """
        Check that the objects in the file have the necessary fields and types for the parsers to work.
        Schema set in the config file, but maybe more schemas could be added in the future.
        """
        for item in self.data:
            try:
                jsonschema.validate(instance=item, schema=config.schema)
            except jsonschema.exceptions.ValidationError as e:
                logger.error(
                    "Input file contains records that don't match the required schema: {}".format(
                        e
                    )
                )

    @property
    def headers_text(self):
        return self._get_headers_text()

    @property
    def headers_indices(self):
        return self._get_headers_indices()

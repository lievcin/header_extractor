import logging
import sys

sys.path.append(".")
logger = logging.getLogger(__name__)

from src.config import config
from parsers.base import Parser
import re


WORD = re.compile(r"\w+")
HEADER_THRESHOLD = config.jaccard["threshold"]


def tokenize(text):
    """
    Simplistic implementation of a tokenizer, done in order to avoid NLTK dependencies at this stage.
    """
    text = text.lower()
    tokens = WORD.findall(text)
    tokens = [t for t in tokens if t.isalpha()]
    return tokens


def mod_jaccard_similarity(list1, list2):
    """
    Modified Jaccard distance, output is the % of the first list that is contained in the second one.
    """
    s1 = set(list1)
    s2 = set(list2)
    return float(len(s1.intersection(s2)) / max(len(s1), 1))


class JaccardParser(Parser):
    """
    Parser that reads the paragraphs sequentially and classifies an item as a header if the proportion
    of it's tokenized representation is contained in the next paragraph is above a predefined threshold.
    """

    def __init__(self, path):
        super().__init__(path)

    def _get_headers_text(self):
        """
        Identifies paragraph text if it satisfies a threshold of tokens contained in the next paragraph.
        """
        headers_text = []
        l1_tokens = []
        for item in self.data:
            l2_text = item["p_text"]
            l2_tokens = tokenize(item["p_text"])
            if mod_jaccard_similarity(l1_tokens, l2_tokens) > HEADER_THRESHOLD:
                headers_text.append(l1_text)
            l1_text, l1_tokens = l2_text, l2_tokens
        return headers_text

    def _get_headers_indices(self):
        """
        Identifies paragraph indices if the corresponding text satisfies a threshold of tokens contained in the next paragraph.
        """
        headers_indices = []
        l1_tokens = []
        for item in self.data:
            l2_index = item["p_id"]
            l2_tokens = tokenize(item["p_text"])
            if mod_jaccard_similarity(l1_tokens, l2_tokens) > HEADER_THRESHOLD:
                headers_indices.append(l1_index)
            l1_index, l1_tokens = l2_index, l2_tokens
        return headers_indices

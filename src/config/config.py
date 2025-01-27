schema = {
    "type": "object",
    "properties": {"p_id": {"type": "number"}, "p_text": {"type": "string"}},
    "required": ["p_id", "p_text"],
}

regex = [
    {"pattern": "\d+ [A-Z ]+"},
    {"pattern": "[A-Z][A-Z \-]+$|\d+. [A-Z][a-zA-Z ]+"},
]

jaccard = {"threshold": 0.33}

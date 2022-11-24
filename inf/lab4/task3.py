import re
from task1 import Token, TokenType, obj2xml, parse_tokens


def tokenise(s: str):
    return [
        Token(match.group(match.lastindex), TokenType(match.lastindex + 1))
        for match in re.finditer('|'.join([
            r'(\{)',
            r'(\})',
            r'(\[)',
            r'(\])',
            r'"((?:\.|[^"])*)"',
            r'(:)',
            r'(,)',
        ]), s)
    ]


def parse_json(s: str):
    tokens = tokenise(s)
    res = parse_tokens(iter(tokens))
    return res


def task3(s: str):
    res = parse_json(s)
    return obj2xml(res)

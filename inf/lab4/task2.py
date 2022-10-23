import json
from dict2xml import dict2xml


def parse_json(s: str):
    return json.loads(s)


def obj2xml(s: str):
    return dict2xml(s)


def task2(s: str):
    res = parse_json(s)
    return obj2xml(res)

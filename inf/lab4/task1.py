from dataclasses import dataclass
from enum import Enum, auto
from pathlib import Path
import pprint
from typing import Iterator


class TokenType(Enum):
    NONE = auto()
    BEGIN_OBJ = auto()
    END_OBJ = auto()
    BEGIN_ARR = auto()
    END_ARR = auto()
    STR = auto()
    COL = auto()
    COMMA = auto()


@dataclass(init=True)
class Token:
    val: str
    type: TokenType


def tokenise(s: str):
    tokens: list[Token] = []

    it = iter(s)
    while True:
        try:
            i = next(it)
        except StopIteration:
            break
        cur = Token(i, TokenType.NONE)
        match i:
            case '{': cur.type = TokenType.BEGIN_OBJ
            case '}': cur.type = TokenType.END_OBJ
            case '[': cur.type = TokenType.BEGIN_ARR
            case ']': cur.type = TokenType.END_ARR
            case ':': cur.type = TokenType.COL
            case ',': cur.type = TokenType.COMMA
            case '"':
                cur.type = TokenType.STR
                cur.val = ''
                while True:
                    try:
                        i = next(it)
                    except StopIteration:
                        break
                    if i == "\\":
                        i = next(it)
                    elif i == '"':
                        break
                    cur.val += i

        if cur.type != TokenType.NONE:
            tokens.append(cur)

    return tokens


def parse_tokens(it: Iterator[Token]):
    i = next(it)
    match i.type:
        case TokenType.STR:
            return i.val
        case TokenType.BEGIN_OBJ:
            res = {}
            i = next(it)
            while True:
                if i.type != TokenType.STR:
                    raise RuntimeError('expected str key')
                key = i.val
                i = next(it)
                if i.type != TokenType.COL:
                    raise RuntimeError('expected `:`')
                val = parse_tokens(it)
                res[key] = val
                i = next(it)
                if i.type == TokenType.COMMA:
                    i = next(it)
                elif i.type == TokenType.END_OBJ:
                    break
                else:
                    raise RuntimeError('unexpected token')
            return res
        case TokenType.BEGIN_ARR:
            res = []
            while True:
                val = parse_tokens(it)
                res.append(val)
                i = next(it)
                if i.type == TokenType.COMMA:
                    continue
                elif i.type == TokenType.END_ARR:
                    break
                else:
                    raise RuntimeError('unexpected token')
            return res


def parse_json(s: str):
    tokens = tokenise(s)
    res = parse_tokens(iter(tokens))
    return res


def obj2xml(obj, deep=0, parent='root') -> str:
    sp = '  ' * deep
    match obj:
        case str(): return obj
        case dict():
            res = ''
            for (key, val) in obj.items():
                match val:
                    case list():
                        res += obj2xml(val, deep+1, key)
                    case str():
                        res += f'{sp}<{key}>{val}</{key}>\n'
                    case _:
                        res += f'{sp}<{key}>\n{obj2xml(val, deep+1, key)}{sp}</{key}>\n'
            return res
        case list():
            return ''.join(f'{sp}<{parent}>{obj2xml(val, deep+1)}</{parent}>\n' for val in obj)


def task1(s: str):
    res = parse_json(s)
    return obj2xml(res)

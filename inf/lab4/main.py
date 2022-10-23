from enum import Enum, auto
from pprint import pprint
from typing import Iterator, List


class TokenType(Enum):
    NONE = auto()
    BEGIN_OBJ = auto()
    END_OBJ = auto()
    BEGIN_ARR = auto()
    END_ARR = auto()
    STR = auto()
    COL = auto()
    COMMA = auto()


class Token:
    val: str
    type: TokenType

    def __init__(self) -> None:
        self.type = TokenType.NONE

    def __repr__(self) -> str:
        return str(self.__dict__)


def tokenise(s: str):
    tokens: list[Token] = []
    cur = Token()

    it = iter(s)
    while True:
        try:
            i = next(it)
            cur.val = i
            match i:
                case '{':
                    cur.type = TokenType.BEGIN_OBJ
                case '}':
                    cur.type = TokenType.END_OBJ
                case '[':
                    cur.type = TokenType.BEGIN_ARR
                case ']':
                    cur.type = TokenType.END_ARR
                case ':':
                    cur.type = TokenType.COL
                case ',':
                    cur.type = TokenType.COMMA
                case '"':
                    cur.type = TokenType.STR
                    cur.val = ''
                    while True:
                        try:
                            i = next(it)
                            if i == '\\':
                                i = next()
                            if i == '"':
                                break
                            cur.val += i
                        except StopIteration:
                            break
            if cur.type != TokenType.NONE:
                tokens.append(cur)
                cur = Token()
        except StopIteration:
            break
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
                    raise RuntimeError("expected str key")
                key = i.val
                i = next(it)
                if i.type != TokenType.COL:
                    raise RuntimeError("expected `:`")
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


def parse_json(s):
    tokens = tokenise(s)
    res = parse_tokens(iter(tokens))
    return res

def obj2xml(obj):
    res = ''
    if type(obj) is str:
        res = obj
    elif type(obj) is dict:
        for (key, val) in obj.items():
            res += f'<{key}>{obj2xml(val)}</{key}>'
    elif type(obj) is list:
        for val in obj:
            res += f'<{key}>{obj2xml(val)}</{key}>'
        

def main():
    s = open('/home/wgmlgz/itmo/inf/lab4/input.json').read()
    res = parse_json(s)
    open('/home/wgmlgz/itmo/inf/lab4/out.json', mode='w+').write(str(res))


if __name__ == "__main__":
    main()

class ParserError(Exception):
    def __init__(self, msg, position):
        self.position = position
        super().__init__(msg)


class UnexpectedCharacterError(ParserError):
    def __init__(self, char, position):
        self.char = char
        self.position = position
        super().__init__(
            f"Unexpected character '{char}' at position {position+1}", position
        )


class MissingTerminalError(ParserError):
    def __init__(self, expected, position):
        self.expected = expected
        self.position = position
        super().__init__(
            f"Missing terminal '{expected}' at position {position+1}", position
        )


class LL1Parser:
    def __init__(self):
        self.parsing_table = {
            "S": {"a": ["A", "B", "C"], "c": ["A", "B", "C"]},
            "A": {"a": ["a", "A", "a"], "c": ["c"]},
            "B": {"b": ["b", "B'"]},
            "B'": {"a": ["a", "B'"], "b": ["b", "B'"], "c": [], "$": []},
            "C": {"c": ["c", "C'"]},
            "C'": {"c": ["c", "C''"], "$": []},
            "C''": {"c": ["c", "A"], "b": ["B", "B"]},
        }

        self.follow = {"B'": {"b", "c", "$"}, "C'": {"c", "$"}, "C''": {"c", "$"}}

    def parse(self, input_str):
        stack = ["$", "S"]
        input = list(input_str) + ["$"]
        ptr = 0
        error_log = []

        while stack[-1] != "$":
            top = stack[-1]
            current_char = input[ptr] if ptr < len(input) else "$"

            if top == current_char:
                stack.pop()
                ptr += 1
                continue

            if top in self.parsing_table:
                productions = self.parsing_table[top].get(current_char, None)
                # print(top, current_char)
                # print(productions, stack)
                if productions is None:
                    # Handle epsilon transitions using FOLLOW sets
                    if top in ["B'", "C'", "C''"] and current_char in self.follow.get(
                        top, set()
                    ):
                        stack.pop()
                        continue
                    else:
                        self.handle_error(top, current_char, ptr, input_str, error_log)
                        continue

                stack.pop()
                if productions != []:  # Non-epsilon production
                    stack.extend(reversed(productions))
            else:
                self.handle_error(top, current_char, ptr, input_str, error_log)
                continue

        if error_log:
            raise ParserError("\n".join(error_log))
        return True

    def handle_error(self, top, current_char, position, input_str, error_log):
        # Error 1: Unexpected character
        if top in self.parsing_table and current_char not in self.parsing_table[top]:
            error_msg = f"Unexpected character '{current_char}' at position {position}. Expected one of: {list(self.parsing_table[top].keys())}"
            error_log.append(error_msg)
            raise UnexpectedCharacterError(current_char, position)

        # Error 2: Missing required terminal
        if top.islower() or top == "$":
            error_msg = f"Missing '{top}' at position {position}"
            error_log.append(error_msg)
            raise MissingTerminalError(top, position)

        # General error case
        error_log.append(
            f"Syntax error at position {position} near '{input_str[max(0, position-2):position+1]}'"
        )
        raise ParserError("Syntax error")


# Tests
def test_parser(print_dbg):
    parser = LL1Parser()
    test_cases = [
        ("acabc", True),                  # Ok
        ("acbc", False),                  # Missing a
        ("aaacaaabbbbbbbbacccccc", True), # Ok
        ("abc", False),                   # Invalid syntax
        ("acabx", False),                 # Unexpected character 'x'
        ("ac", False),                    # Missing terminals
        ("aabcc", False),                 # Invalid structure
    ]

    for idx, (input_str, expected) in enumerate(test_cases):

        try:
            parser.parse(input_str)
            dbg = f"Input: '{input_str}' => Valid"
            result = True
        except ParserError as e:
            pref = "Input: '"
            dbg = pref + f"{input_str}' => Error:" + "\n"
            dbg += " " * (len(pref) + e.position) + f"^ {e}"
            result = False
        # print(expected, result)
        print(f"Test {idx+1}: " + ("Ok" if expected == result else "Fail"))
        if print_dbg:
          print(dbg)


if __name__ == "__main__":
    test_parser(True)

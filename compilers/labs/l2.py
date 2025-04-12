class DFA:
    def __init__(self, rules, final_states):
        self.rules = rules
        self.final_states = final_states

    def check_seq(self, curr_state, seq: str) -> bool:
        for ch in seq:
            if ch in self.rules[curr_state]:
                curr_state = self.rules[curr_state][ch]
            else:
                return False
        return curr_state in self.final_states

    def run_tests(self, tests):
        all_passed = True
        for counter, (seq, expected) in enumerate(tests.items()):
            result = self.check_seq("S", seq)
            if result == expected:
                pass
            else:
                print(f"Test {counter}: Input string: '{seq}'")
                all_passed = False
                print(f"FAILED (expected {expected}, got {result})")
                print("=" * 30)
        if all_passed:
            print("ALL TESTS PASSED")
        else:
            print("SOME TESTS FAILED")
        print("=" * 30)


def main():
    rules = {
        "S": {"a": "S", "b": "E", "c": "S"},
        "E": {"a": "S", "b": "E", "c": "S"},
    }
    final_states = ["E"]

    tests = {
        "abc": False,
        "a": False,
        "ab": True,
        "bb": True,
        "babb": True,
        "bc": False,
        "cabb": True,
        "bca": False,
        "bcbc": False,
        "ccab": True,
    }

    dfa = DFA(rules, final_states)
    dfa.run_tests(tests)


if __name__ == "__main__":
    main()

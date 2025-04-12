# Множество строк четной длины, которые содержат ровно один a.
# S → bC | cC | aB
# A → bB | cB
# B → b | c | bA | cA
# C → bS | cS | aA | a


class DFA:
    def __init__(self, rules, final_states):
        self.rules = rules
        self.final_states = final_states

    def check_seq(self, curr_state, seq: str) -> bool:
        for ch in seq:
            prev_state = curr_state
            if ch in self.rules[curr_state]:
                curr_state = self.rules[curr_state][ch]
            else:
                return False
        return seq[-1] in self.final_states[prev_state]

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
        "S": {"b": "C", "c": "C", "a": "B"},
        "A": {"b": "B", "c": "B"},
        "B": {"b": "A", "c": "A"},
        "C": {"b": "S", "c": "S", "a": "A"},
    }
    final_states = {"S": "", "A": "", "B": "bc", "C": "a"}

    tests = {
        "abc": False,
        "a": False,
        "ab": True,
        "ba": True,
        "babc": True,
        "bb": False,
        "cabc": True,
        "bca": False,
        "bcbc": False,
        "ccab": True,
    }

    dfa = DFA(rules, final_states)
    dfa.run_tests(tests)


if __name__ == "__main__":
    main()

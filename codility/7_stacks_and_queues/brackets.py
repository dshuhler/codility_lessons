import unittest


def solution(S):

    bracket_stack = []

    for char in S:
        if char in {"(", "[", "{"}:
            bracket_stack.append(char)
        else:
            if len(bracket_stack) == 0:
                return 0
            last_open = bracket_stack.pop()
            if ((char == ")" and last_open == "(")
                    or (char == "]" and last_open == "[")
                    or (char == "}" and last_open == "{")):
                continue
            else:
                return 0
    if len(bracket_stack) == 0:
        return 1
    else:
        return 0


class TestTriangle(unittest.TestCase):

    def test_true_sample(self):
        self.assertEqual(1, solution("{[()()]}"))

    def test_false_sample(self):
        self.assertEqual(0, solution("([)()]"))

    def test_odd(self):
        self.assertEqual(0, solution("([["))

    def test_start_closed(self):
        self.assertEqual(0, solution(")()"))


if __name__ == '__main__':
    unittest.main()

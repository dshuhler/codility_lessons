import unittest


def solution(S):

    bracket_stack = []

    for char in S:
        if char in {"(", "[", "{"}:
            bracket_stack.append(char)
        else:
            last_open = bracket_stack.pop()
            if ((char == ")" and last_open == "(")
                    or (char == "]" and last_open == "[")
                    or (char == "}" and last_open == "{")):
                continue
            else:
                return 0
    return 1


class TestTriangle(unittest.TestCase):

    def test_true_sample(self):
        self.assertEqual(1, solution("{[()()]}"))

    def test_false_sample(self):
        self.assertEqual(0, solution("([)()]"))


if __name__ == '__main__':
    unittest.main()

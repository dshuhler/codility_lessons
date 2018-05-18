import unittest


def solution(S):

    num_open_brackets = 0

    for char in S:
        if char == "(":
            num_open_brackets += 1
        else:
            if num_open_brackets == 0:
                return 0
            else:
                num_open_brackets -= 1

    if num_open_brackets == 0:
        return 1
    else:
        return 0


class TestTriangle(unittest.TestCase):

    def test_true_sample(self):
        self.assertEqual(1, solution("(()(())())"))

    def test_false_sample(self):
        self.assertEqual(0, solution("())"))

    def test_odd(self):
        self.assertEqual(0, solution("((("))

    def test_start_closed(self):
        self.assertEqual(0, solution(")()"))


if __name__ == '__main__':
    unittest.main()

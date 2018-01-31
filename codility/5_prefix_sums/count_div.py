import unittest


def next_divisible_by(value, divisor):
    if value % divisor == 0:
        return value

    times = (value // divisor)

    return (times + 1) * divisor


def prev_divisible_by(value, divisor):
    times = (value // divisor)
    return times * divisor


def solution(A, B, K):

    last = prev_divisible_by(B, K)
    first = next_divisible_by(A, K)

    difference = last - first
    return (difference // K) + 1


class TestCountDiv(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(3, solution(6, 11, 2))

    def test_edges(self):
        self.assertEqual(4, solution(0, 15, 5))
        self.assertEqual(3, solution(1, 15, 5))
        self.assertEqual(1, solution(3, 13, 7))
        self.assertEqual(2, solution(5, 15, 7))


if __name__ == '__main__':
    unittest.main()

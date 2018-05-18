import unittest

# You COULD solve this by sorting, but using a set has the same time complexity and is cleaner


def solution(A):
    unique_values = set(A)
    return len(unique_values)


class TestDistinct(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(3, solution([2, 1, 1, 2, 3, 1]))

    def test_big_all_same(self):
        self.assertEqual(1, solution([1] * 100000))

    def test_big_sequence(self):
        self.assertEqual(100000, solution(range(100000)))

import unittest

# Note: Python's sort algo is "Timsort" - a hybrid of merge sort and insertion sort


def solution(A):
    A.sort()  # I'd rather use sorted() and not modify the input but rules says I can't use additional memory
    return max(A[-3] * A[-2] * A[-1], A[0] * A[1] * A[-1])


class TestMaxProductOfThree(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(60, solution([-3, 1, 2, -2, 5, 6]))

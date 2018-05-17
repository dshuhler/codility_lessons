import unittest


def solution(A):

    smallest_start_index = 0
    smallest_avg = None
    current_avg = None

    for index, value in enumerate(A):

        this_slice = A[smallest_start_index:index]
        current_avg = sum(this_slice) / len(this_slice)
        if current_avg > smallest_avg:
            smallest_avg = current_avg


class TestMinAvgTwoSlice(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(1, solution([4, 2, 2, 5, 1, 5, 8]))

    def test_small_big_small(self):
        self.assertEqual(0, solution([5, 500, 1, 500]))

    def test_small(self):
        self.assertEqual(0, solution([5]))

    def test_same(self):
        self.assertEqual(0, solution([5, 5, 5, 5, 5]))


import unittest

# The trick to this problem is to realize that any min slice is going to have a length of 2 or 3. Any slice larger than
# that will be able to be broken down into smaller slices. It is guaranteed that one of these smaller slice will be <=
# the big slice.
#
# knowing this allows us to move across the array checking all the slices 2 - 3 in length (linear time). You don't even
# have to use prefix sums.


def slice_avg(vals, start_index, length):
    total = sum(vals[start_index:start_index + length])
    return total / length


def solution(A):

    min_index = 0
    min_value = 10001

    for idx in range(0, len(A) - 1):
        if slice_avg(A, idx, 2) < min_value:
            min_index = idx
            min_value = slice_avg(A, idx, 2)
        if idx < len(A) - 2 and slice_avg(A, idx, 3) < min_value:
            min_index = idx
            min_value = slice_avg(A, idx, 3)

    return min_index


class TestMinAvgTwoSlice(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(1, solution([4, 2, 2, 5, 1, 5, 8]))

    def test_small_big_small(self):
        self.assertEqual(0, solution([5, 500, 1, 500]))

    def test_small(self):
        self.assertEqual(0, solution([5]))

    def test_same(self):
        self.assertEqual(0, solution([5, 5, 5, 5, 5]))

    def test_two_elements(self):
        self.assertEqual(0, solution([5, 5]))

    def test_four_elements(self):
        self.assertEqual(2, solution([1, 5, 1, 1]))

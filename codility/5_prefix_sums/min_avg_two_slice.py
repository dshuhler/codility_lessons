import unittest

# The trick to this problem is to realize that any min slice is going to have a length of 2 or 3. Any slice larger than
# that will be able to be broken down into smaller slices. It is guaranteed that one of these smaller slice will be <=
# the big slice.
#
# knowing this allows us to move across the array checking all the slices 2 - 3 in length (linear time). You don't even
# have to use prefix sums, but I did anyway :)


def prefix_sums(vals):
    result = [0] * len(vals)
    current_sum = 0
    for i, val in enumerate(vals):
        current_sum += val
        result[i] = current_sum
    return result


def solution(A):

    psums = prefix_sums(A)

    smallest_start_index = 0
    smallest_avg = 0

    for i in range(len(A) - 1):

        if i == 0:
            two_slice_avg = psums[1] / 2
            three_slice_avg = psums[2] / 3
            if two_slice_avg < three_slice_avg:
                smallest_avg = two_slice_avg
            else:
                smallest_avg = three_slice_avg
        else:
            two_slice_avg = (psums[i + 1] - psums[i - 1]) / 2
            if two_slice_avg < smallest_avg:
                smallest_start_index = i
                smallest_avg = two_slice_avg
            if i < len(A) - 2:
                three_slice_avg = (psums[i + 2] - psums[i - 1]) / 3
                if three_slice_avg < smallest_avg:
                    smallest_start_index = i
                    smallest_avg = three_slice_avg

    return smallest_start_index


class TestMinAvgTwoSlice(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(1, solution([4, 2, 2, 5, 1, 5, 8]))

    def test_small_big_small(self):
        self.assertEqual(0, solution([5, 500, 1, 500]))

    def test_small(self):
        self.assertEqual(0, solution([5]))

    def test_same(self):
        self.assertEqual(0, solution([5, 5, 5, 5, 5]))


import unittest


def solution(A):
    # don't recalculate every time, just keep a running total of left/right
    # values and increment/decrement them as you iterate over array

    left_total = A[0]
    right_total = sum(A[1:])

    min_difference = abs(left_total - right_total)

    for num in A[1:len(A) - 1]:
        left_total += num
        right_total -= num
        min_difference = min(min_difference, abs(left_total - right_total))
    return min_difference


class TestTapeEquilibrium(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(solution([3, 1, 2, 4, 3]), 1)

    def test_big_negative(self):
        self.assertEqual(solution([-1000, 1000]), 2000)


if __name__ == '__main__':
    unittest.main()
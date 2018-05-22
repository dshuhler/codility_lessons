import unittest


def solution(A):

    prefixes = [0] * len(A)
    suffixes = [0] * len(A)

    for i in range(1, len(A) - 1):
        prefixes[i] = max(prefixes[i - 1] + A[i], 0)

    for i in range(len(A) - 2, 1, -1):
        suffixes[i] = max(suffixes[i + 1] + A[i], 0)

    max_sum = 0

    for i in range(1, len(A) - 1):
        max_sum = max(max_sum, prefixes[i - 1] + suffixes[i + 1])

    return max_sum


class TestMaxProfit(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(17, solution([3, 2, 6, -1, 4, 5, -1, 2]))


if __name__ == '__main__':
    unittest.main()
import unittest


def solution(A):

    max_val = A[0]
    ending_val = A[0]

    for i in range(1, len(A)):
        ending_val = max(A[i], ending_val + A[i])
        max_val = max(max_val, ending_val)

    return max_val


class TestMaxProfit(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(5, solution([3, 2, -6, 4, 0]))

    def test_one_neg(self):
        self.assertEqual(-100, solution([-100]))


if __name__ == '__main__':
    unittest.main()
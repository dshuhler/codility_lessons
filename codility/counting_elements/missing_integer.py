import unittest


def solution(A):
    found_positive_ints = [False] * len(A)
    for num in A:
        if 0 < num <= len(A):
            found_positive_ints[num - 1] = True

    for index, val in enumerate(found_positive_ints):
        if not val:
            return index + 1

    return len(A) + 1


class TestMissingInteger(unittest.TestCase):

    def test_samples(self):
        self.assertEqual(solution([1, 2, 3]), 4)
        self.assertEqual(solution([-1, -3]), 1)
        self.assertEqual(solution([1, 3, 6, 4, 1, 2]), 5)

    def test_n_max(self):
        biglist = list(range(1, 100000))
        self.assertEqual(100000, solution(biglist))

    def test_big_num_small_array(self):
        self.assertEqual(1, solution([50000]))


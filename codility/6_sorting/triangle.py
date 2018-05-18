import unittest


def is_triangular(triplet):
    return ((triplet[0] + triplet[1] > triplet[2])
            and (triplet[1] + triplet[2] > triplet[0])
            and (triplet[0] + triplet[2] > triplet[1]))


def solution(A):
    A.sort()

    for i in range(len(A) - 2):
        if is_triangular(A[i: i + 3]):
            return 1

    return 0


class TestTriangle(unittest.TestCase):

    def test_true_sample(self):
        self.assertEqual(1, solution([10, 2, 5, 1, 8, 20]))

    def test_false_sample(self):
        self.assertEqual(0, solution([10, 50, 5, 1]))


if __name__ == '__main__':
    unittest.main()

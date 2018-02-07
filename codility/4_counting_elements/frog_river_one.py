import unittest


def solution(X, A):
    leaf_coverage = [False] * X
    frog_position = -1
    for time, fallen_leaf_position in enumerate(A):
        leaf_coverage[fallen_leaf_position - 1] = True

        for num in range(frog_position, X):
            if leaf_coverage[frog_position + 1]:
                frog_position += 1
                if frog_position + 1 == X:
                    return time
            else:
                break

    return -1


class TestPassingCars(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(6, solution(5, [1, 3, 2, 4, 3, 3, 5, 2]))

    def test_not_able_to_cross(self):
        self.assertEqual(-1, solution(5, [1, 3, 2, 4, 3, 3, 4, 2]))

    def test_big_river(self):
        self.assertEqual(100000, solution(100001, list(range(0, 100001))))


if __name__ == '__main__':
    unittest.main()



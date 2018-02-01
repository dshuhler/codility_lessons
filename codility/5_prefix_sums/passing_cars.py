import unittest


def solution(A):

    eastward_cars = 0
    passed_cars = 0

    for car in A:
        if car == 0:
            eastward_cars += 1
        else:
            passed_cars += eastward_cars

        if passed_cars > 1000000000:  # one billion
            return -1

    return passed_cars


class TestPassingCars(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(5, solution([0, 1, 0, 1, 1]))

    def test_no_passes(self):
        self.assertEqual(0, solution([1, 1, 1, 1, 0, 0, 0, 0]))

    def test_almost_too_big(self):
        self.assertEqual(999990000, solution([0] * 10000 + [1] * 99999))

    def test_too_big(self):
        self.assertEqual(-1, solution([0] * 99999 + [1] * 9999))

    def test_small(self):
        self.assertEqual(0, solution([0]))
        self.assertEqual(0, solution([1]))


if __name__ == '__main__':
    unittest.main()

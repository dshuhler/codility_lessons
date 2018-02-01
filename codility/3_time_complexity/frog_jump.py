import unittest


def solution(X, Y, D):
    distance = Y - X
    jumps = (distance // D)
    if distance % D != 0:
        jumps += 1
    return jumps


class TestPassingCars(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(3, solution(10, 85, 30))

    def test_no_distance(self):
        self.assertEqual(0, solution(10, 10, 1))

    def test_max_jump(self):
        self.assertEqual(1, solution(1, 2, 1000000000))

    def test_max_num_jumps(self):
        self.assertEqual(1000000000, solution(0, 1000000000, 1))


if __name__ == '__main__':
    unittest.main()

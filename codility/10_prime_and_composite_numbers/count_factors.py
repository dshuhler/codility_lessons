import unittest


def solution(N):
    i = 1
    num_factors = 0

    while (i * i) < N:
        if N % i == 0:
            num_factors += 2
        i += 1

    if (i * i) == N:
        num_factors += 1

    return num_factors


class TestCountFactors(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(8, solution(24))


if __name__ == '__main__':
    unittest.main()
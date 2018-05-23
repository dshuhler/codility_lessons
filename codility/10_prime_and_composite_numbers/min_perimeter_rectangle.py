import unittest


def largest_low_factor(N):
    i = 1
    largest_factor = 1

    while (i * i) < N:
        if N % i == 0:
            largest_factor = i
        i += 1

    if (i * i) == N:
        largest_factor = i

    return largest_factor


def solution(N):
    side_a = largest_low_factor(N)
    side_b = N // side_a
    return (side_a + side_b) * 2


class TestMinPerimeterRectangle(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(22, solution(30))


if __name__ == '__main__':
    unittest.main()
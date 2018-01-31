import unittest


def solution(N):

    # convert to binary string
    binary_s = "{0:b}".format(N)

    this_length = 0
    max_length = 0

    for c in binary_s:
        if c == '1':
            max_length = max(max_length, this_length)
            this_length = 0
        else:
            this_length += 1

    return max_length


class TestBinaryGap(unittest.TestCase):

    def test_samples(self):
        self.assertEqual(solution(9), 2)
        self.assertEqual(solution(529), 4)
        self.assertEqual(solution(1041), 5)

    def test_no_gap(self):
        self.assertEqual(solution(6), 0)
        self.assertEqual(solution(15), 0)

    def test_zero(self):
        self.assertEqual(solution(0), 0)


if __name__ == '__main__':
    unittest.main()

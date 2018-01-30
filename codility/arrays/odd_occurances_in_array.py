import unittest


def solution(A):

    # since we need to have constant space complexity, our only solution is a
    # XOR trick - albeit a pretty cool one

    missing_int = 0
    for value in A:
        missing_int = missing_int ^ value
    return missing_int


class TestMissingInteger(unittest.TestCase):

    def test_samples(self):
        self.assertEqual(solution([9, 3, 9, 3, 9, 7, 9]), 7)

    def test_long(self):
        self.assertEqual(solution(list(range(1, 500000)) * 2 + [999999]), 999999)


if __name__ == '__main__':
    unittest.main()

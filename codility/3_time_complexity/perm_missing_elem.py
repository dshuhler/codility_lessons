import unittest


def solution(A):
    index_total = 0
    value_total = 0

    for index, value in enumerate(A):
        index_total += index + 1
        value_total += value

    return (index_total - value_total) + len(A) + 1


class TestPermMissingElem(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(4, solution([2, 1, 3, 5]))

    def test_sequential(self):
        self.assertEqual(4, solution([1, 2, 3, 5, 6]))

    def test_non_sequential(self):
        self.assertEqual(9, solution([2, 1, 3, 5, 6, 7, 8, 10, 4]))

    def test_big(self):
        big_list = list(range(1, 1000000))
        big_list.remove(400)
        self.assertEqual(400, solution(big_list))


if __name__ == '__main__':
    unittest.main()

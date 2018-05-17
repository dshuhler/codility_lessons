import unittest


def solution(A):
    occurances = [0] * len(A)

    for num in A:
        if num > len(A):
            return 0
        elif occurances[num - 1] == 1:
            return 0
        else:
            occurances[num - 1] = 1
    return 1


class TestPermCheck(unittest.TestCase):

    def test_true_sample(self):
        self.assertEqual(1, solution([4, 1, 2, 3]))

    def test_false_sample(self):
        self.assertEqual(0, solution([4, 1, 3]))

    def test_multiple_missing(self):
        self.assertEqual(0, solution([4, 10, 3]))

    def test_one_to_ten_randomized(self):
        self.assertEqual(1, solution([4, 10, 3, 1, 2, 5, 6, 7, 9, 8]))

    def test_big_with_missing(self):
        big_list = list(range(1, 100000))
        big_list.remove(400)
        self.assertEqual(0, solution(big_list))

    def test_big_reverse_order(self):
        big_list = list(range(100000, 0, -1))
        self.assertEqual(1, solution(big_list))


if __name__ == '__main__':
    unittest.main()
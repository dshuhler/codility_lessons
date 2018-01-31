import unittest


def solution(A, K):

    # handle case where array is empty
    if len(A) == 0:
        return []

    # find the number of times we ACTUALLY need to shift (we can ignore
    # multiples of the size of the array since that will just produce the
    # same result)
    defacto_shift = K % len(A)

    # swap front and back of array based on the size of the shift
    rotation_point = len(A) - defacto_shift
    shifted_front = A[rotation_point:]
    shifted_back = A[:rotation_point]

    return shifted_front + shifted_back


class TestCyclicRotation(unittest.TestCase):

    def test_samples(self):
        self.assertEqual(solution([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])
        self.assertEqual(solution([1, 2, 3, 4, 5], 1), [5, 1, 2, 3, 4])

    def test_empty_array(self):
        self.assertEqual(solution([], 1), [])

    def test_big_array(self):
        self.assertEqual(solution(list(range(1, 101)), 1), [100] + list(range(1, 100)))


if __name__ == '__main__':
    unittest.main()

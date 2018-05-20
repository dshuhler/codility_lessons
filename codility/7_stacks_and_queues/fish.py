import unittest


def solution(A, B):

    upstream_fish = []
    surviving_downstream_fish = 0

    for i, direction in enumerate(B):
        size = A[i]
        if direction == 1:
            upstream_fish.append(size)
        else:
            eaten = False

            if len(upstream_fish) > 0:
                for j in range(len(upstream_fish)):
                    if size > upstream_fish[-1]:
                        upstream_fish.pop(-1)
                    else:
                        eaten = True
                        break

            if not eaten:
                surviving_downstream_fish += 1

    return surviving_downstream_fish + len(upstream_fish)


class TestFish(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(2, solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))

    def test_more_upstream(self):
        self.assertEqual(3, solution([4, 3, 1, 5, 2, 6, 7], [1, 0, 1, 0, 1, 0, 0]))


if __name__ == '__main__':
    unittest.main()

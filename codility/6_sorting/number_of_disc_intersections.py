import unittest


def solution(A):
    disc_edges = []
    for i, radius in enumerate(A):
        disc_edges.append((i - radius, True))
        disc_edges.append((i + radius, False))

    disc_edges.sort(key=lambda x: (x[0], not x[1]))

    num_intersections = 0
    active_circles = 0

    for _, is_edge_start in disc_edges:
        if is_edge_start:
            num_intersections += active_circles
            active_circles += 1
        else:
            active_circles -= 1

        if num_intersections > 10000000:
            return -1

    return num_intersections


class TestNumberOfDiscIntersections(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(11, solution([1, 5, 2, 1, 4, 0]))

    def test_three(self):
        self.assertEqual(3, solution([1, 1, 1]))


if __name__ == '__main__':
    unittest.main()

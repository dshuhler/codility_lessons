import unittest

# The trick here is to not scan the whole array of counters every time you
# need to set them all to the max value, which leads to 0n^2 complexity in
# worst cases.


def solution(N, A):
    counters = [0] * N
    individual_counter_max = 0
    val_min = 0

    for num in A:
        if 1 <= num <= N:

            if counters[num - 1] < val_min:
                counters[num - 1] = val_min

            counters[num - 1] += 1

            if counters[num - 1] > individual_counter_max:
                individual_counter_max = counters[num - 1]

        elif num > N:
            val_min = individual_counter_max

    for index, counter in enumerate(counters):
        if counter < val_min:
            counters[index] = val_min

    return counters


class TestMaxCounters(unittest.TestCase):

    def test_sample(self):
        self.assertEqual([3, 2, 2, 4, 2], solution(5, [3, 4, 4, 6, 1, 4, 4]))

    def test_big_nums(self):
        self.assertEqual(solution(100000, list(range(1, 100001))), [1] * 100000)


if __name__ == '__main__':
    unittest.main()

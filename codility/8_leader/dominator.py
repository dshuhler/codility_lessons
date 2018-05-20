import unittest


def is_dominator(candidate, list):
    count = 0
    for val in list:
        if val == candidate:
            count += 1
    return count > len(list) // 2


def solution(A):
    dominator_stack = []

    for num in A:
        if dominator_stack and num != dominator_stack[-1]:
            dominator_stack.pop()
        else:
            dominator_stack.append(num)

    if dominator_stack and is_dominator(dominator_stack[0], A):
        for i, num in enumerate(A):
            if num == dominator_stack[0]:
                return i
    else:
        return -1


class TestDominator(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(0, solution([3, 2, 3, 4, 3, 3, 3, -1]))

    def test_no_dominator(self):
        self.assertEqual(-1, solution([1, 2, 3, 4, 5, 6]))

    def test_empty(self):
        self.assertEqual(-1, solution([]))


if __name__ == '__main__':
    unittest.main()
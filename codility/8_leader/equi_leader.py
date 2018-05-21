import unittest


def is_dominator(candidate, list):
    count = 0
    for val in list:
        if val == candidate:
            count += 1
    return count > len(list) // 2


def find_leader(leader_list):
    leader_stack = []

    for num in leader_list:
        if leader_stack and num != leader_stack[-1]:
            leader_stack.pop()
        else:
            leader_stack.append(num)

    if leader_stack and is_dominator(leader_stack[0], leader_list):
        return leader_stack[0]
    else:
        return -1


def solution(A):
    leader = find_leader(A)
    if leader == -1:
        return 0

    right_leader_count = A.count(leader)
    left_leader_count = 0
    array_length = len(A)
    equi_leader_count = 0

    for i, val in enumerate(A):
        if val == leader:
            left_leader_count += 1
            right_leader_count -= 1

        right_leader = right_leader_count > (array_length - (i + 1)) // 2
        left_leader = left_leader_count > (i + 1) // 2

        if right_leader and left_leader:
            equi_leader_count += 1

    return equi_leader_count


class TestEquiLeader(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(2, solution([4, 3, 4, 4, 4, 2]))


if __name__ == '__main__':
    unittest.main()
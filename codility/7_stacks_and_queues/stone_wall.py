import unittest


def solution(H):
    block_stack = []
    current_height = 0
    num_blocks = 0

    for height in H:
        if height > current_height:
            block_stack.append(height - current_height)
            num_blocks += 1
            current_height = height
        elif height < current_height:
            while height < current_height:
                popped_block = block_stack.pop()
                current_height -= popped_block
            if height > current_height:
                block_stack.append(height - current_height)
                num_blocks += 1
                current_height = height

    return num_blocks


class TestTriangle(unittest.TestCase):

    def test_true_sample(self):
        self.assertEqual(7, solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))


if __name__ == '__main__':
    unittest.main()

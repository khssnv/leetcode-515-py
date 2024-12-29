from typing import List, Optional
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largest_values(self, root: Optional[TreeNode]) -> List[int]:
        ...


class TestSolution(unittest.TestCase):
    def test_input_1(self):
        # * * * 1 * * *
        # * 3 * * * 2 *
        # 5 * 3 * * * 9
        root = TreeNode(
            1,
            TreeNode(
                3,
                TreeNode(5),
                TreeNode(3),
            ),
            TreeNode(
                2,
                None,
                TreeNode(9),
            ),
        )
        solution = Solution()
        self.assertEqual(solution.largest_values(root), [1, 3, 9])

    def test_input_2(self):
        # * 1 *
        # 2 * 3
        root = TreeNode(
            1,
            TreeNode(2),
            TreeNode(3),
        )
        solution = Solution()
        self.assertEqual(solution.largest_values(root), [1, 3])


if __name__ == '__main__':
    unittest.main()

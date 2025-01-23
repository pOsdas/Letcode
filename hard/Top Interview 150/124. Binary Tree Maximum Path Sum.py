class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')

        def calculate(node):
            if not node:
                return 0

            left_sum = max(calculate(node.left), 0)
            right_sum = max(calculate(node.right), 0)

            current_value = left_sum + right_sum + node.val

            self.max_sum = max(current_value, self.max_sum)

            return node.val + max(left_sum, right_sum)

        calculate(root)
        return self.max_sum







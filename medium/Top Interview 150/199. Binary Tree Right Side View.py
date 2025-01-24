from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        result = []
        queue = deque([root])
        result.append(root.val)
        level_size = len(queue)

        while queue:
            num = float('inf')
            for i in range(len(queue)):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                    num = current.left.val
                if current.right:
                    queue.append(current.right)
                    num = current.right.val

            if num != float('inf'):
                result.append(num)

        return result

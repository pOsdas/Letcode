from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        bool_var = False

        while queue:
            sublist = []
            level_size = len(queue)

            for i in range(level_size):
                current = queue.popleft()
                sublist.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            if bool_var:
                sublist.reverse()

            result.append(sublist)
            bool_var = not bool_var

        return result


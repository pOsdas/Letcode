class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return

        while root:
            if root.left:
                mostright = root.left
                while mostright.right:
                    mostright = mostright.right
                mostright.right = root.right
                root.right = root.left
                root.left = None

            root = root.right





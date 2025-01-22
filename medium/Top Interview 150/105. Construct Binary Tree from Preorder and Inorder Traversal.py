class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        def build(preorder, inorder):
            if not preorder or not inorder:
                return None

            root_val = preorder[0]
            root = TreeNode(root_val)

            root_index = inorder.index(root_val)

            root.left = build(preorder[1:1 + root_index], inorder[:root_index])
            root.right = build(preorder[1 + root_index:], inorder[root_index + 1:])

            return root

        root = build(preorder, inorder)
        return root

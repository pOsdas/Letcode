# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(
            self,
            inorder: list[int],
            postorder: list[int]
    ) -> TreeNode:

        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}

        def build(inStart, inEnd, postStart, postEnd):
            if inStart > inEnd or postStart > postEnd:
                return None

            root_val = postorder[postEnd]
            root = TreeNode(root_val)

            rootIndex = inorder_index_map[root_val]

            leftSize = rootIndex - inStart

            root.left = build(inStart, rootIndex - 1, postStart, postStart + leftSize - 1)
            root.right = build(rootIndex + 1, inEnd, postStart + leftSize, postEnd - 1)

            return root

        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getDepth(r):
            if not r:
                return 0
            return max(getDepth(r.left), getDepth(r.right))+1

        if not root:
            return 0

        ld = getDepth(root.left)
        rd = getDepth(root.right)
        d = ld+rd

        return max(d, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
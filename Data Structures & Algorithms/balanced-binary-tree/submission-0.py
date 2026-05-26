# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getDepth(r):
            if not r:
                return 0
            return max(getDepth(r.left), getDepth(r.right))+1

        if not root:
            return True
        if abs(getDepth(root.left) - getDepth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
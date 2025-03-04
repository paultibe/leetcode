# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
                return True
        def maxDepth(root):
            if not root:
                return 0
            
            return 1 + max(maxDepth(root.left), maxDepth(root.right))
        
        if abs(maxDepth(root.right) - maxDepth(root.left)) > 1:
            return False
        return self.isBalanced(root.right) and self.isBalanced(root.left)
        
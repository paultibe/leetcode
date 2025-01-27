# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMaxDepth(self, root: Optional[TreeNode], depth: int) -> int:
        if not root:
            return depth
        return max(self.getMaxDepth(root.right, depth + 1), self.getMaxDepth(root.left, depth + 1))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.getMaxDepth(root.left, 1), self.getMaxDepth(root.right, 1)) 
        
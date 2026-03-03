class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0 
            
        left, right = self.maxDepth(root.left), self.maxDepth(root.right)

        return 1 + max(left, right)
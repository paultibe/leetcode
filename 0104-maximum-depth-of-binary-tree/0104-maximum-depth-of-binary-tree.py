class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0 
        def dfs(node, current_depth):
            if not node.right and not node.left:
                return current_depth
            
            left, right = 0, 0
            if node.left:
                left = dfs(node.left, current_depth + 1)
            if node.right:
                right = dfs(node.right, current_depth + 1)

            return max(left, right)
                        
        return dfs(root, 1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        # if on oppostie sides or one side and root, LCA is the root
        # case 2: if both on left (both values are smaller than root.val)
        # case 3: if both on right
        """
        def dfs(root):
            if min(p.val, q.val) <= root.val and max(p.val, q.val) >= root.val:
                return root
            if p.val < root.val and q.val < root.val:
                return dfs(root.left)
            else: # bothOnRight
                return dfs(root.right)
        return dfs(root)

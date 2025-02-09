# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # p isn't necessarily < q

        curr = root
        while(curr):
            if min(p.val, q.val) <= curr.val and max(p.val, q.val) >= curr.val:
                return curr
            if max(p.val, q.val) < curr.val:
                curr = curr.left
            else:
                curr = curr.right




        # follow ups: what if p and q don't exist in the tree?
        
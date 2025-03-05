# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # path between node at max depths of both subtrees
        # go all the way doww -> THIS IS POSTORDER TRAVERSAL
        maxDiameter = 0

        def dfs(root):
            nonlocal maxDiameter
            if not root:
                return 0
            # update diameter at every step
            heightRight = dfs(root.right)
            heightLeft = dfs(root.left)
            maxDiameter = max(maxDiameter, heightRight + heightLeft)
            return 1 + max(heightRight, heightLeft)
        dfs(root)
        return maxDiameter 
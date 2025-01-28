# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if not root:
            return root

        # do computation
        temp = root.right
        root.right = root.left
        root.left = temp

        # repeat. this can handle null children
        self.invertTree(root.right)
        self.invertTree(root.left)

        # when it's all done, return 
        return root
        


        
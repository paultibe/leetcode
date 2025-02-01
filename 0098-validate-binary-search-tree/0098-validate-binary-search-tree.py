# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # cannot check directly against parent, so must add parameter
        def isValid(root, lower, upper):
            # base case 
            if not root:
                return True 
            # do computation
            nodeIsValid = root.val > lower and root.val < upper
            if not (nodeIsValid):
                return False
            # recurse
            return isValid(root.right, root.val, upper) and isValid(root.left, lower, root.val)
        return isValid(root, float("-inf"), float("inf"))
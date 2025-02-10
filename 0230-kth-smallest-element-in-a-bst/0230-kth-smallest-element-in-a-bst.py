# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sortedVals = []
        def inOrderTraversal(root):
            # base case
            if not root:
                return
            # recurse in order
            inOrderTraversal(root.left)
            sortedVals.append(root.val)
            inOrderTraversal(root.right)
        
        inOrderTraversal(root)
        return sortedVals[k - 1]
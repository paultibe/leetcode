# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 1 ,2 , 3, 4
        # result[k - 1]
        nodesToTraverse = k
        result = root.val
        def inOrderDfs(root):
            # base case
            nonlocal nodesToTraverse
            nonlocal result
            if not root:
                return 
            inOrderDfs(root.left)
            nodesToTraverse -= 1
            if nodesToTraverse == 0:
                result = root.val
                return
            inOrderDfs(root.right)
        
        inOrderDfs(root)
        return result
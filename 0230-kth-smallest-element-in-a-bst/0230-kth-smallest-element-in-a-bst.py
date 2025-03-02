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
        result = []
        nodesToTraverse = k
        def inOrderDfs(root, nodesToTraverse):
            # base case
            if not root:
                return 
            inOrderDfs(root.left, nodesToTraverse)
            result.append(root.val)
            nodesToTraverse -= 1
            # if nodesToTraverse == 0:
            #     # return result[k - 1]
            inOrderDfs(root.right, nodesToTraverse)
        
        inOrderDfs(root, nodesToTraverse)
        return result[k - 1]
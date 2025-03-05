# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        res = []
        q = collections.deque([root])
        
        while q:
            qLen = len(q)
            
            for i in range(qLen):
                node = q.popleft()
                
                # Only add to result when it's the last node in current level
                if i == qLen - 1:
                    res.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS, level order traversal
        queue = deque()

        if root:
            queue.append(root)
        
        level = 0
        while queue:
            # go level by level
            for i in range(len(queue)):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            # only increment when you've visited all nodes on level
            level += 1
        
        return level 
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # keep a todo list
        result = []
        if not root:
            return result
        todo = deque()
        todo.append(root)

        while todo:
            currentLevel = []
            for i in range(len(todo)):
                node = todo.popleft()
                currentLevel.append(node.val)
                if node.left:
                    todo.append(node.left)
                if node.right:
                    todo.append(node.right)
            result.append(currentLevel)
        
        return result
        
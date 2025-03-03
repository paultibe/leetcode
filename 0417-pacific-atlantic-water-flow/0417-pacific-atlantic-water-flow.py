class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def bfs(r, c, prevVal):
            nonlocal pacific, atlantic
            queue = deque()
            queue.append((r, c, float('inf')))
            visited = set()
            while queue:
                for i in range(len(queue)):
                    row, col, prev = queue.popleft()
                    if row < 0 or col < 0:
                        pacific = True
                        break
                    if row >= ROWS or col >= COLS:
                        atlantic = True
                        break
                    if heights[row][col] > prev or (row, col) in visited:
                        break
                    
                    visited.add((row, col))
                    for dx, dy in directions:
                        queue.append((row + dx, col + dy, heights[row][col]))
                        if pacific and atlantic:
                            break
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                pacific = False
                atlantic = False
                bfs(r, c, float('inf'))
                if pacific and atlantic:
                    res.append([r, c])
        return res

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs
        ROWS = len(grid)
        COLS = len(grid[0])
        # top, left, right, bottom
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        result = 0
        visit = set() # (x, y)
        # iterate through entire grid
        def bfs(cell):
            # todo list
            queue = deque()
            queue.append(cell)
            while queue:
                row, col = queue.popleft()
                for direction in directions:
                    # obtain each neighbour
                    newRow = row + direction[0]
                    newCol = col + direction[1]
                    newCell = (newRow, newCol)
                    if (newCell not in visit
                        and newRow < ROWS
                        and newCol < COLS
                        and newCol >= 0
                        and newRow >= 0
                        and grid[newRow][newCol] == "1"):
                            queue.append(newCell)
                            visit.add(newCell)
            
        for row in range(ROWS):
            for col in range(COLS):
                if (grid[row][col] == "1" and (row, col) not in visit):
                    bfs((row, col))
                    result += 1
        
        return result




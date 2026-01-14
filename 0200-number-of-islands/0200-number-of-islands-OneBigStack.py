class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        stack = [] # one big stack

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    stack.append((r, c))
                    grid[r][c] = "0"
                    
                    while stack:
                        curr_r, curr_c = stack.pop()
                        
                        for dr, dc in directions:
                            nr, nc = curr_r + dr, curr_c + dc
                            
                            if (0 <= nr < ROWS and 
                                0 <= nc < COLS and 
                                grid[nr][nc] == "1"):
                                
                                grid[nr][nc] = "0"
                                stack.append((nr, nc))
        return islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            for dr, dc in directions:
                newRow = r + dr
                newCol = c + dc
                if (newRow < 0 or newCol < 0 or newRow >= ROWS or
                newCol >= COLS or grid[newRow][newCol] == "0"):
                    continue
                grid[newRow][newCol] = "0"
                dfs(newRow, newCol)
                

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    grid[r][c] == "0"
                    dfs(r, c)
                    islands += 1

        return islands
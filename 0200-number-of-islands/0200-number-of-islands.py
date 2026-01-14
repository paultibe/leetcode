class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            stack = [(r, c)]

            while stack:
                newR, newC = stack.pop()
                if (newR < 0 or newC < 0 or newR >= ROWS or
                    newC >= COLS or grid[newR][newC] == "0"
                ):
                    continue

                grid[newR][newC] = "0"
                for dr, dc in directions:
                    stack.append((newR + dr, newC + dc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands
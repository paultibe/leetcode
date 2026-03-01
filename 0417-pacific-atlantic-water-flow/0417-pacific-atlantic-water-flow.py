class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pacific = atlantic = False

        def dfs(r, c):
            nonlocal pacific, atlantic

            original_value = heights[r][c]
            heights[r][c] = float('inf')
            for dx, dy in directions:
                new_row = r + dx
                new_col = c + dy
                if new_row >= ROWS or new_col >= COLS:
                    atlantic = True
                    continue
                if new_row < 0 or new_col < 0:
                    pacific = True
                    continue
                if heights[new_row][new_col] > original_value:
                    continue
                if pacific and atlantic:
                    break
                dfs(new_row, new_col)
            heights[r][c] = original_value

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                pacific = False
                atlantic = False
                dfs(r, c)
                if pacific and atlantic:
                    res.append([r, c])
        return res
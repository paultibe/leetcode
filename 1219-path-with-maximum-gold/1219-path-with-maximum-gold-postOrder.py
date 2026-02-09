class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        # clockwise from right
        toNext = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        maximumGold = 0

        # pre-validated dfs
        # base case is that there's no valid neighbours, returns gold
        def dfs(row, column):
            temp = grid[row][column]
            grid[row][column] = 0
            result = temp
            for toNextRow, toNextColumn in toNext:
                nextRow = row + toNextRow
                nextColumn = column + toNextColumn
                if (0 <= nextRow < ROWS) and (0 <= nextColumn < COLUMNS) and grid[nextRow][nextColumn] > 0:
                    result = max(result, temp + dfs(nextRow, nextColumn))
            grid[row][column] = temp # post order step
            return result

        for row in range(ROWS):
            for column in range(COLUMNS):
                if grid[row][column] > 0:
                    maximumGold = max(maximumGold, dfs(row, column))
        
        return maximumGold
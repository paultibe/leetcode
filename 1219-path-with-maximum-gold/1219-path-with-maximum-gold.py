class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        # clockwise from right
        toNext = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        maximumGold = 0

        # pre-validated dfs
        def dfs(row, column, gold):
            gold += grid[row][column] # pre-order step
            temp = grid[row][column]
            grid[row][column] = 0
            result = gold
            for toNextRow, toNextColumn in toNext:
                nextRow = row + toNextRow
                nextColumn = column + toNextColumn
                if (0 <= nextRow < ROWS) and (0 <= nextColumn < COLUMNS) and grid[nextRow][nextColumn] > 0:
                    result = max(result, dfs(nextRow, nextColumn, gold))
            grid[row][column] = temp # post order step
            return result

        for row in range(ROWS):
            for column in range(COLUMNS):
                if grid[row][column] > 0:
                    maximumGold = max(maximumGold, dfs(row, column, 0))
        
        return maximumGold


        # base case is that there's no valid neighbours?
        # 6, 14, max(19, 23, 21)
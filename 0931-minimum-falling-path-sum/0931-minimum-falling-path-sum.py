class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        ROWS = len(matrix)
        COLS = len(matrix[0])

        min_sum_of_falling_path = float("inf")
        @cache
        def minimumSumStartingWith_StartingAt(row, col):
            current_value = matrix[row][col]
            if row == ROWS - 1:
                return current_value
            left, down, right = float("inf"), float("inf"), float("inf")
            if 0 <= col - 1 < COLS:
                left = minimumSumStartingWith_StartingAt(row + 1, col - 1) + current_value
            down = minimumSumStartingWith_StartingAt(row + 1, col) + current_value
            if 0 <= col + 1 < COLS:
                right = minimumSumStartingWith_StartingAt(row + 1, col + 1) + current_value
            return min(left, down, right)

        for i in range(COLS):
            min_sum_of_falling_path = min(min_sum_of_falling_path, minimumSumStartingWith_StartingAt(0, i))
        return min_sum_of_falling_path
        
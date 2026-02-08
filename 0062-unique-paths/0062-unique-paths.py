class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dfs(i, j):
            if i == (m - 1) and j == (n - 1):
                return 1
            right = 0
            down = 0
            if j < n - 1:
                right = dfs(i, j + 1)
            if i < m - 1:
                down = dfs(i + 1, j)
            return right + down

        return dfs(0, 0)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = defaultdict(int)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == (m - 1) and j == (n - 1):
                    cache[(i,j)] = 1
                    continue
                right = 0
                down = 0
                if j < n - 1:
                    right = cache[(i, j + 1)]
                if i < m - 1:
                    down = cache[(i + 1, j)]
                cache[(i, j)] = right + down

        return cache[(0, 0)]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = defaultdict(int)
        cache[(m-1, n-1)] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                right = cache[(i, j + 1)]
                down = cache[(i + 1, j)]
                # "+" for the m-1, n-1 case
                cache[(i, j)] += right + down

        return cache[(0, 0)]
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        subproblems = [0 for i in range(n + 1)]
        subproblems[n] = 1
        subproblems[n - 1] = 1
        for i in range(n - 2, -1, -1):
            subproblems[i] = subproblems[i + 1] + subproblems[i + 2]
        return subproblems[0]
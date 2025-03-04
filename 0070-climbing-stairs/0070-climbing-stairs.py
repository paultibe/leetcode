class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        twoSteps = 1
        oneStep = 1
        for i in range(n - 1):
            temp = oneStep
            oneStep = oneStep + twoSteps
            twoSteps = temp
        return oneStep
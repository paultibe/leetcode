class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def climb(currentStep):
            option1 = 0
            if currentStep > n:
                return 0
            if currentStep == n:
                return 1
            if currentStep in cache:
                return cache[currentStep]
            cache[currentStep] = climb(currentStep + 1) + climb(currentStep + 2)
            return cache[currentStep]
        
        return climb(0)
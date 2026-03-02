from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        S = sum(nums)
        if abs(target) > S: return 0
        n = len(nums)

        # A single dictionary where keys are (current_sum, index)
        dp = defaultdict(int)

        # Base Case: At the "back" (index n), 
        # reaching the target sum is the only success.
        dp[(target, n)] = 1

        # Build the table backwards
        for i in range(n - 1, -1, -1):
            for s in range(-S, S + 1):
                # To calculate dp[(s, i)], we look at the results
                # we already stored for index i + 1.
                dp[(s, i)] = dp[(s + nums[i], i + 1)] + dp[(s - nums[i], i + 1)]

        # The answer is starting at sum 0 and index 0
        return dp[(0, 0)]
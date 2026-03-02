from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        S = sum(nums)
        if abs(target) > S: return 0
        n = len(nums)

        dp = defaultdict(int)
        dp[(target, n)] = 1

        for index in range(n - 1, -1, -1):
            for current_sum in range(-S, S + 1):
                add = dp[(current_sum + nums[index], index + 1)]
                subtract = dp[(current_sum - nums[index], index + 1)]
                
                dp[(current_sum, index)] = add + subtract

        return dp[(0, 0)]
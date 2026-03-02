from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @cache
        def dfs(current_sum, index):
            add_current = current_sum + nums[index]
            sub_current = current_sum - nums[index]
            if index == len(nums) - 1:
                return (add_current == target) + (sub_current == target)
            add = dfs(current_sum + nums[index], index + 1)
            subtract = dfs(current_sum - nums[index], index + 1)
            return add + subtract
        
        return dfs(0, 0)
        
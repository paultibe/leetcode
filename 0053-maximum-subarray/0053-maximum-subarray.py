class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0
        def dfs(i):
            nonlocal curSum
            nonlocal maxSub
            if i == len(nums):
                return 0
            if curSum < 0:
                curSum = 0
            curSum += nums[i]
            maxSub = max(maxSub, curSum)
            dfs(i+1)
        dfs(0)
        return maxSub
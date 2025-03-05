class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        if len(nums) == 1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[len(nums)-1] # that last one will be storing the max
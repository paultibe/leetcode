class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def rob(index):
            if index >= len(nums):
                return 0
            if index in cache:
                return cache[index]
            cache[index] = max(rob(index + 1), nums[index] + rob(index + 2))
            return cache[index]

        return rob(0)
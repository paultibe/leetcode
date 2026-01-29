class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        cache = defaultdict(int)

        def dfs(i):
            if i == len(nums):
                return 0
            
            if i in cache:
                return cache[i]

            # try all valid next elements
            for j in range(i + 1, len(nums)):
                # special starting case
                if i == -1 or nums[i] < nums[j]:
                    cache[i] = max(cache[i], 1 + dfs(j))

            return cache[i]

        return dfs(-1)
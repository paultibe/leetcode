class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = defaultdict(bool)
        cache[(len(nums) - 1)] = True

        for i in range(len(nums) - 1, - 1, - 1):
            farthest_jump = min(len(nums) - 1, nums[i] + i)
            for jump in range(i + 1, farthest_jump + 1):
                if cache[jump]:
                    cache[i] = cache[jump]
                    break
            # all jumps exhausted
            # defaults to False

        return cache[0]    
 
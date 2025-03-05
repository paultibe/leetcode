class Solution:
    def rob(self, nums: List[int]) -> int:
        doublePrevHouse = nums[0]
        if len(nums) == 1:
            return doublePrevHouse
        prevHouse = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = prevHouse
            prevHouse = max(prevHouse, nums[i] + doublePrevHouse)
            doublePrevHouse = temp

        return prevHouse
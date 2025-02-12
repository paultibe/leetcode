class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        productOfNumsBeforeCurrentNum = 1
        for i in range(len(nums)):
            result[i] *= productOfNumsBeforeCurrentNum
            productOfNumsBeforeCurrentNum *= nums[i]

        productOfNumsAfterCurrentNum = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= productOfNumsAfterCurrentNum
            productOfNumsAfterCurrentNum *= nums[i]
        
        return result
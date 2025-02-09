class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        beforeList = [[1] for i in range(len(nums))] 
        productOfNumsBefore = 1
        for i in range(len(nums)):
            beforeList[i] = productOfNumsBefore
            productOfNumsBefore *= nums[i]
        
        afterList = [1] * len(nums)
        productsOfNumsAfter = 1
        for i in range(len(nums) - 1, -1 , -1):
            afterList[i] = productsOfNumsAfter
            productsOfNumsAfter *= nums[i]

        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = afterList[i] * beforeList[i]

        return result 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 1, 1

        for num in nums:
            prevMax = curMax
            
            extendPositive = num * prevMax
            extendNegative = num * curMin # The "Redemption" (Negative * Negative)
            startNew       = num
            
            curMax = max(extendPositive, extendNegative, startNew)
            
            shrinkNegative = num * prevMax
            shrinkPositive = num * curMin
            startNewMin    = num
            
            curMin = min(shrinkNegative, shrinkPositive, startNewMin)
            
            res = max(res, curMax)
            
        return res
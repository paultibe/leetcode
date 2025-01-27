class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        # sliding window approach
        left = 0
        right = 0

        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            diff = prices[right] - prices[left]
            if diff > maxProfit:
                maxProfit = diff

        return maxProfit
        
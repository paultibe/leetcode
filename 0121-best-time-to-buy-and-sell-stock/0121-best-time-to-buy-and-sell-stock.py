class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force approach 
        maxProfit = 0
        for i in range (1, len(prices)):
            for j in range (i - 1, 0, -1):
                diff = prices[i] - prices[j]
                if (diff > maxProfit):
                    maxProfit = diff

        return maxProfit
        
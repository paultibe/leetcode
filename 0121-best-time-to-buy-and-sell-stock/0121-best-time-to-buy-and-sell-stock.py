class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force
        result = 0
        for day1 in range(len(prices)):
            for day2 in range(day1, len(prices)):
                profit = prices[day2] - prices[day1]
                result = max(result, profit)
        return result
        
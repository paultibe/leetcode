class Solution:
    def maxArea(self, height: List[int]) -> int:
        # BRUTE FORCE
        # result = 0
        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         currentAmount = min(height[i], height[j]) * (j-i)
        #         result = max(result, currentAmount)
        
        # return result   

        # TWO POINTERS
        # criteria for selecting new left pillar: 
        # added height > loss width
        # (height[j] - height[i]) > (j - i)
        result = 0
        left = 0
        right = len(height) - 1

    while (left < right):
        # Calculate current area
        currentAmount = min(height[right], height[left]) * (right - left)
        result = max(result, currentAmount)
        if height[right] < height[left]:
            right -= 1
        else:
            left += 1

        return result
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Initializing pointers and the sliding window sum
        left = 0
        current_sum = 0
        
        # Build the initial window of size k
        for right in range(k):
            current_sum += nums[right]
            
        max_sum = current_sum
        
        # Slide the window using explicit right and left pointers
        # 'right' moves forward by 1 each step
        for right in range(k, len(nums)):
            # Add the new element entering from the right
            current_sum += nums[right]
            
            # Subtract the element exiting from the left
            current_sum -= nums[left]
            
            # Increment left to maintain the window size k
            left += 1
            
            # Update max_sum if the new window is larger
            if current_sum > max_sum:
                max_sum = current_sum
                
        return max_sum / k
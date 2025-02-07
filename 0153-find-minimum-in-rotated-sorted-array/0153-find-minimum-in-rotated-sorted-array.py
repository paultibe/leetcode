class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        while (left <= right):
            mid = (left + right) // 2
            # compare to mid to its left value
            if nums[mid] < nums[mid - 1]:
                # you've found it!
                return nums[mid]
            # if search space isn't sorted, direct search closer to pivot point
            if nums[mid] > nums[right]:
                left = mid + 1
            # search space is sorted, go left
            else:
                right = mid - 1
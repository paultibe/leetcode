class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # a lot of conditionals that determine where to guide search space!
        left, right = 0, len(nums) - 1
        while (left <= right):
            mid = (left + right) // 2 # can also left + ((right - left) / 2)
            if nums[mid] == target:
                return mid

            # left sorted portion
            if nums[mid] >= nums[left]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid -1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        # not found
        return -1
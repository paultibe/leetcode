class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # a lot of conditionals that determine where to guide search space!
        left, right = 0, len(nums) - 1
        while (left <= right):
            mid = (left + right) // 2 # can also left + ((right - left) / 2)
            if nums[mid] == target:
                return mid

            # mid is greater
            if (nums[mid] > target): 
                if ((nums[left] <= nums[mid] and target >= nums[left]) or nums[left] > nums[mid]:
                    right = mid - 1
                # after pivot
                else:
                    left = mid + 1
            # mid is smaller
            else:
                if (nums[left] <= nums[mid] or target <= nums[right]):
                    left = mid + 1
                # after pivot
                else:
                    right = mid - 1

        # not found
        return -1
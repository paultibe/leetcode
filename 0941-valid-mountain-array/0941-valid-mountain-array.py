class Solution:
    def validMountainArray(self, arr):
        n = len(arr)
        if n < 3:
            return False

        def find_peak(nums):
            i = 0
            while i + 1 < len(nums) and nums[i] < nums[i+1]:
                i += 1
            return i

        def is_descending(nums, peak_index):
            # means peak wasn't peak of mountain but just cliff
            if peak_index == 0 or peak_index == len(nums) - 1:
                return False
            
            for i in range(peak_index, len(nums) - 1):
                if nums[i] <= nums[i+1]:
                    return False
            return True

        peak_index = find_peak(arr)
        return is_descending(arr, peak_index)
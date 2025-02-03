class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            # skip duplicates (this is why sorting helps, can compare with previous element)
            if i > 1 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while (left < right):
                currentSum = nums[i] + nums[left] + nums[right]
                if currentSum < 0:
                    left += 1
                elif currentSum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    # but you can't have duplicates, so have to move one of the pointers
                    while (nums[left] == nums[left - 1] and left < right):
                        left += 1
        return result


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # BOYER-MOORE. not intuitive

        count = 1
        candidate = nums[0]

        for num in nums:
            if num == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = num
                    count = 2
        
        return candidate 
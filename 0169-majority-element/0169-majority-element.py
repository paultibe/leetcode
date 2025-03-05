class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        [2,2,1,1,1,2,2,2,2]
        """
        count = 1
        maybeMajority = nums[0]

        for num in nums:
            if num == maybeMajority:
                count += 1
            else:
                count -= 1
                if count == 0:
                    maybeMajority = num
                    count = 2
        
        return maybeMajority
            

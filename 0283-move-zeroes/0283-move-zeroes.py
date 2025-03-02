class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # EXAMPLE
        # [1, 0,1,0,3,12]
        # [1, 1,3,12, 0, 0]
        # [1, 1,3,12,0,0]
        # two pointer approach
        # leftMostZero
        # read 
        # do not return anything

        leftMostZero = 0 
        for read in range(len(nums)):
            if nums[read] != 0:
                if leftMostZero == read:
                    # not at a zero, move both pointers
                    leftMostZero += 1
                    continue
                # otherwise, swap 
                nums[leftMostZero], nums[read] = nums[read], nums[leftMostZero]
                leftMostZero += 1

        
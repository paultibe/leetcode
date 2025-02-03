class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # time: 
        # space: O(n)
        if not nums:
            return 0
        # somehow need to count each sequence within nums array
        result = 1
        numbers = set(nums)

        for num in numbers:
            # detect new sequence
            if (num - 1) not in numbers:
                currentSequence = 0
                while (num + currentSequence) in numbers:
                    currentSequence += 1
                result = max(result, currentSequence)
        return result 
        
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            # Create a 'snapshot' of the current result using list() or [:]
            # This prevents the loop from seeing the subsets we are about to add
            for i in range(len(result)):
                subset = result[i]
                new_subset = subset + [num] # Concise way to copy and add
                result.append(new_subset)
        
        return result
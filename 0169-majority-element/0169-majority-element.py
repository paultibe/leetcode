class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # NAIVE SOLUTION
        counts = Counter(nums) # could use defaultdict(lambda: 0)
        # gives you key value pairs (as tuples) and then sort
        sortedCounts = sorted(counts.items(), key = lambda x: x[1]) # sort based on counts NOT numbers themselves
        return sortedCounts.pop()[0]
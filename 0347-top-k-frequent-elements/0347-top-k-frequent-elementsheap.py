class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # USING LIST
        counts = {}
        # counts
        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
        
        sorted_counts = sorted(counts.items(), key = lambda mappings: mappings[1])

        result = []
        for i in range(k):
            result.append(sorted_counts.pop()[0])

        return result
        # USING HEAP

        

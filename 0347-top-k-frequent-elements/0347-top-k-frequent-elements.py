class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sorting
        counts = {}
        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
        result = []
        for i, cnt in counts.items():
            result.append((cnt, i))
        
        result.sort() # (1, 5), (2, 3), (4, 8)
        result2 = []
        for i in range(k):
            result2.append(result.pop()[1])
        
        return result2





        

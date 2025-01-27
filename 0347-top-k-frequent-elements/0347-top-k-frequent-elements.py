class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # USING HEAP
        # time: nlogk
        # space: n

        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        heap = [] # by default min heap

        for num, count in counts.items():
            heappush(heap, (-count, num))
        
        result = []
        for i in range(k):
            result.append((heappop(heap)[1]))
        return result 


        

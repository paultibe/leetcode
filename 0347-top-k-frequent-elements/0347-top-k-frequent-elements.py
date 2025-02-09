class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # get counts first
        # 5: 3
        # 2: 3
        # 1: 8
        # 4: 7
        counts = {}
        for num in nums:
            counts[num]= counts.get(num, 0) + 1 # can throw KeyError. use TryGetValue
        
        # place into buckets. dictionary with counts as keys, array of elements as values
        # 3: 5, 2
        # 7: 4
        # 8: 1
        buckets = [[] for i in range(len(nums) + 1)]
        for num, cnt in counts.items():
            buckets[cnt].append(num)

        # extract values out of dictionary based on keys
        # dict.keys() -> 3, 7, 8
        result = []
        for i in range(len(buckets)): # need to iterate back across entire list if all elements appear only once
            values = buckets.pop()
            while values:
                result.append(values.pop())
                if len(result) == k:
                    return result






        

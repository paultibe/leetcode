class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # create mappings of values -> counts
        counts = Counter(nums)
        # for num in nums:
        # counts[num] = counts.get(num, 0) + 1
        sorted_items = sorted(list(counts.items()),key = lambda x: x[1])

        return sorted_items.pop()[0]


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        numberToNextGreater = defaultdict(lambda: -1)

        for num in nums2:
            while stack and num > stack[-1]:
                numberToNextGreater[stack.pop()] = num
            stack.append(num)

        return [numberToNextGreater[num] for num in nums1]
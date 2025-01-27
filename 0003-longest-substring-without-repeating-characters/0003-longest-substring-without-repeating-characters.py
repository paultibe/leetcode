class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        left = 0
        right = 0
        substring = set()
        for right in range(len(s)):
            while s[right] in substring:
                substring.remove(s[left])
                left += 1
            substring.add(s[right])
            if len(substring) > maxLength:
                maxLength = len(substring)
        return maxLength
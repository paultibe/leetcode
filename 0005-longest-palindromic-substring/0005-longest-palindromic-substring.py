class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        cache = {}

        def isPalindrome(left, right):
            if s[left] == s[right] and (right - left <= 2 or cache[(left + 1, right - 1)]):
                    cache[(left, right)] = True
                    return True
            cache[(left, right)] = False
            return False

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    if (j - i + 1) > len(res):
                        res = s[i : j + 1]
        return res
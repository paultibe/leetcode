class Solution:
    def longestPalindrome(self, s: str) -> str:
        resultLength = 0
        resultLeft = 0
        cache = {}

        def isPalindrome(left, right):
            # if one or two characters, after first condition, you know you have palindrome
            isPalindrome = s[left] == s[right] and ((right - left <= 2) or cache[(left + 1, right - 1)])
            cache[(left, right)] = isPalindrome
            return isPalindrome

        for j in range(len(s)):
            for i in range(j + 1):
                if isPalindrome(i, j):
                    if (j - i + 1) > resultLength:
                        resultLeft = i
                        resultLength = j - i + 1
                        
        return s[resultLeft : resultLeft + resultLength]
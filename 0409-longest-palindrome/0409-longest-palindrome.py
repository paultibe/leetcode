class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        result = 0
        hasOdd = False
        for character in counts:
            if (counts[character] % 2 == 0):
                result += counts[character]
            else:
                # same thing but one less
                result += counts[character] - 1
                hasOdd = True
        if hasOdd:
            return result + 1
        
        return result
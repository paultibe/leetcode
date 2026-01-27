class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        scratch notes
        checking if palindrome is substring: two cases if moving from middle or outside 
        - from middle: if odd, just start pointers on adjacent characters
        - from outside: end when pointers cross each other

        brute force
        TC: O(n^3)
        SC: O(1)

        improving on BF:
        eg. "babaddaga"
        substrings are composed of other substrings (subproblems)
        many substrings may be composed of the same substring -> overlapping subproblems

        """
        cache = {}

        def isPalindrome(left, right) -> bool:
            # base
            if left > right:
                return True

            # question
            if (left, right) in cache:
                return cache[(left, right)]
            
            # computation
            if s[left] != s[right]:
                return False
                
            # recursive call
            cache[(left, right)] = isPalindrome(left + 1, right - 1)
            return cache[(left, right)]
                    
        longestPalindromicSubstring = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    if len(s[i:j+1]) > len(longestPalindromicSubstring):
                        longestPalindromicSubstring = s[i:j+1]
        
        return longestPalindromicSubstring

"""
retro
- you can always decompose problems into subproblems. this will always help.
- but it's especially helpful when a problem has a recurrence relation. subproblems have same structure as parent problemm (not always the case)
- overlapping subproblems = overlapping state space paths
- if wm engaged, dry run does magical debugging.
- could not catch single character cases. off by 1. pointers can't start different indices
"""
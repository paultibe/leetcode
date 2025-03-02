class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # k = numberOfSwitches
        # BRUTE FORCE SOLUTION
        # for every character in s, iterate through every substring starting at that character, keeping track of character counts in substring in a dictionary
        # keep track of max frequency in local
        # if substring meets condition, update maxLengthSoFar
        # condition is that max frequency <= k

        res = 0
        
        # Check all possible substrings
        for i in range(len(s)):
            for j in range(i, len(s)):
                # For each substring s[i:j+1], calculate counts from scratch
                substring = s[i:j+1]
                length = j - i + 1
                
                # Count character frequencies
                count = Counter(substring)
                # for char in substring:
                    # count[char] = 1 + count.get(char, 0)
                
                # Find most frequent character by sorting
                max_freq = max(count.values())
                # Alternative using sorting:
                # max_freq = sorted(count.items(), key=lambda x: x[1], reverse=True)[0][1] if count else 0
                
                # Check if this is a valid substring with at most k replacements
                if length - max_freq <= k:
                    res = max(res, length)
        
        return res

        # SLIDING WINDOW 
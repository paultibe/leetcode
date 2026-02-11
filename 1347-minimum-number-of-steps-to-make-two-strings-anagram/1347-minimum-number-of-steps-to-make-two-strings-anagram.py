from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # Get counts for both strings
        s_counts = Counter(s)
        t_counts = Counter(t)
        
        steps = 0
        
        # We only care about characters in S
        for char in s_counts:
            if s_counts[char] > t_counts[char]:
                # Sum the "positives" (the extras in s)
                steps += s_counts[char] - t_counts[char]
                
        return steps
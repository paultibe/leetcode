from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)
        
        if s1_length > s2_length:
            return False
            
        target_counts = Counter(s1)

        for i in range(s2_length - s1_length + 1):
            current_substring = s2[i : i + s1_length]
            
            if Counter(current_substring) == target_counts:
                return True
                
        return False
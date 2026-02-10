class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # initially assume the pivot is at index -1 (everything should be 1)
        # suffix is everything after current element
        suffix_zeros = s.count('0')
        # prefix is everything before and including current element
        prefix_ones = 0
        
        min_flips = suffix_zeros 
        
        for char in s:
            if char == '0':
                # no longer in the suffix; 
                suffix_zeros -= 1
            else:
                # current element is part of prefix
                prefix_ones += 1
                
            min_flips = min(min_flips, prefix_ones + suffix_zeros)
            
        return min_flips
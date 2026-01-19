from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        char_counts = Counter(word)
        freq_counts = Counter(char_counts.values())
        unique_freqs = sorted(freq_counts.keys())
        
        if len(unique_freqs) == 1:
            return unique_freqs[0] == 1 or freq_counts[unique_freqs[0]] == 1

        if len(unique_freqs) == 2:
            f1, f2 = unique_freqs
            cnt1, cnt2 = freq_counts[f1], freq_counts[f2]
            
            if f1 == 1 and cnt1 == 1:
                return True
                
            if f2 == f1 + 1 and cnt2 == 1:
                return True
                
        return False